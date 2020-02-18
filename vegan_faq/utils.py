import time
import os
import random

import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
import pandas as pd
from PIL import Image
import requests



@st.cache()
def load_data():
    df = pd.read_csv('vegan_faq/data/vegan_answer_tf2.csv')
    #df = df.loc[df['title'].str[-1] == '?']
    #df.drop('Unnamed: 0', axis = 1, inplace=True)
    return df


@st.cache(allow_output_mutation=True)
def load_model():
    return tf.saved_model.load('vegan_faq/model')


def get_sim(qo, qt, model):
    qs = [qo, qt]
    embed = model(qs)
    sim = np.inner(embed, embed)
    sim = sim[0][1]
    return sim

def comp_q(question, df, model):
    pot_q = df['title']
    pot_a = df['paragraphs']
    similarity = 0
    f_q = ''
    f_a = ''
    for q in pot_q:
        tmp = get_sim(question, q, model)
        if tmp > similarity:
            similarity = tmp
            f_q = q
            f_a = df.loc[df['title'] == q, 'paragraphs']
    return similarity, f_q, f_a


def get_image_url():
    access_key = 'xHH2-pjbPYRwAYLjJ1-1SpdduOIvOd20F_ZR8NLAv_k'
    url = 'https://api.unsplash.com/photos/random/?'
    collection_id = '4224326'
    orientation = 'landscape'
    req_url = url + 'client_id=' + access_key + '&orientation=' + orientation + '&collections=' + collection_id
    req = requests.get(req_url).json()
    photo_link = req['urls']['regular']
    creator = req['user']['name']
    creator_link = req['user']['links']['html']
    return photo_link, creator, creator_link




suggested_questions = ['Does it actually make a difference if I go vegan?',
                           'Do plants feel pain?',
                           'What do vegans think of palm oil?',
                           'Don\'t zoos help protect endangered species?',
                           'If you were stuck on a desert island with just meat, would you eat it?',
                           'What\'s wrong with milking cows?',
                           'Can fish really feel pain like other animals?',
                           'I\'m an athlete, can i go vegan?',
                           'Would you eat road kill?',
                           'Is tattoo ink vegan?',
                           'Is animal testing bad if it benefits humans?']

def select_random_questions(questions):
    q1 = random.choice(questions)
    questions.remove(q1)
    q2 = random.choice(questions)
    questions.remove(q2)
    q3 = random.choice(questions)
    questions.remove(q3)
    q4 = random.choice(questions)
    return q1, q2, q3, q4


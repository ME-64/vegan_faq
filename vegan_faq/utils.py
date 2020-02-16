import streamlit as st
import time
import pandas as pd
import os
import tensorflow as tf
import numpy as np
import pandas as pd
import random
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

@st.cache(show_spinner=False, allow_output_mutation=True)
def load_images():
    imgs = []    
    for i in range(17):
        path = 'vegan_faq/static/img_' + str(i) + '.jpg'
        img = Image.open(path)
        imgs.append(img)
    return imgs


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

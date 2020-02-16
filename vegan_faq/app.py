import streamlit as st
import time
import pandas as pd
from ast import literal_eval
import os
import tensorflow as tf
import numpy as np
import pandas as pd


st.title('SEV - ')
st.title('The Suprisingly Educated Vegan Bot')
st.subheader('Ask me anything!')

place = st.empty()
user_q = place.text_input(label = '') 


def get_sim(qo, qt):
    qs = [qo, qt]
    embed = model(qs)
    sim = np.inner(embed, embed)
    sim = sim[0][1]
    return sim

def comp_q(question, df):
    pot_q = df['title']
    pot_a = df['paragraphs']
    similarity = 0
    f_q = ''
    f_a = ''
    for q in pot_q:
        tmp = get_sim(question, q)
        if tmp > similarity:
            similarity = tmp
            f_q = q
            f_a = df.loc[df['title'] == q, 'paragraphs']
    return similarity, f_q, f_a

@st.cache()
def load_data():
    df = pd.read_csv('vegan_faq/data/vegan_answer_tf.csv')
    #df = df.loc[df['title'].str[-1] == '?']
    #df.drop('Unnamed: 0', axis = 1, inplace=True)
    return df

#@st.cache(hash_funcs = {QAPipeline: QAPipeline.__hash__})
#def load_model(df):
#    cdqa_pipeline = QAPipeline(reader='vegan_faq/bert_qa.joblib')
#    cdqa_pipeline.fit_retriever(df)
#    return cdqa_pipeline

@st.cache(allow_output_mutation=True)
def load_model():
    return tf.saved_model.load('vegan_faq/model')


df = load_data()
model = load_model()

if user_q == '':
    pass

elif len(user_q.split())  < 3:
    st.info('Your question must be more than 3 words')

else:
    with st.spinner('Loading Answer'):
        prediction = comp_q(user_q, df)
        st.success(
            '**Question**\n\n' +
            user_q + '\n\n'
            '**Answer**\n\n' + prediction[2].reset_index(drop=True)[0])
        st.info('Identified Question: ' + prediction[1] + '\n\nConfidence = ' + str(prediction[0]))
        
        

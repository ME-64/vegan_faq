import streamlit as st
import time
import pandas as pd
from ast import literal_eval
import os


from cdqa.utils.filters import filter_paragraphs
from cdqa.utils.download import download_model, download_bnpp_data
from cdqa.pipeline.cdqa_sklearn import QAPipeline

st.title('SEV - ')
st.title('The Suprisingly Educated Vegan Bot')
st.subheader('Ask me anything!')

user_q = st.text_input(label = '') 




#@st.cache()
def load_data():
    df = pd.read_csv('vegan_faq/vegan_qa.csv')
    df['paragraphs'] = df['paragraphs'].str.split('\n')
    df = filter_paragraphs(df, min_length = 5, drop_empty = False)
    return df

#@st.cache(hash_funcs = {QAPipeline: QAPipeline.__hash__})
def load_model(df):
    cdqa_pipeline = QAPipeline(reader='vegan_faq/bert_qa.joblib')
    cdqa_pipeline.fit_retriever(df)
    return cdqa_pipeline


df = load_data()
cdqa_pipeline = load_model(df)

if user_q == '':
    pass

elif len(user_q.split())  < 3:
    st.info('Your question must be more than 3 words')

else:
    with st.spinner('Loading Answer'):
        prediction = cdqa_pipeline.predict(user_q)
        st.success('Answer Found!')
        time.sleep(1)
        st.success('Answer: ' + prediction[0])
        st.success('Context: ' + prediction[2])






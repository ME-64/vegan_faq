import streamlit as st
import time

st.title('SEV - ')
st.title('The Suprisingly Educated Vegan Bot')
st.subheader('Ask me anything!')

user_q = st.text_input(label = '') 


if user_q == '':
    pass

elif len(user_q.split())  < 3:
    st.info('Your question must be more than 3 words')

else:
    with st.spinner('Loading Answer'):
        time.sleep(4)
    st.success('Answer found!')


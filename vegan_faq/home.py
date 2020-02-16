import streamlit as st
import time
import pandas as pd
import os
import tensorflow as tf
import numpy as np
import pandas as pd
import utils

def Home():
    """Home page"""
    
    st.subheader(
            'Have a question about veganism:question:'
            '\nAsk me below and I\'ll try my best to answer!'
            )
    
    
    
    
 
    user_q = st.text_input(label = '')
    ans = st.empty()
    inf = st.empty()
    
    st.markdown('\n\n')
    st.image('vegan_faq/static/img_2.jpg', use_column_width=True)
    
    
    df = utils.load_data()
    model = utils.load_model()
    
    if user_q == '':
        pass
    
    elif len(user_q.split())  < 3:
        st.info('Your question must be more than 3 words')
    
    else:
        with st.spinner('Loading Answer'):
            prediction = utils.comp_q(user_q, df, model)
            ans.success(
                    ':mag: \n**Answer:**\n' + prediction[2].reset_index(drop=True)[0])
            inf.info('Identified Question: ' + prediction[1] + '\n\nConfidence = ' + str(prediction[0]))
            
        

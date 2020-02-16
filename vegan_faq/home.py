import streamlit as st
import time
import pandas as pd
import os
import tensorflow as tf
import numpy as np
import pandas as pd
import utils
import random

def Home():
    """Home page"""
    
    st.subheader(
            'Have a question about veganism:question:'
            )
    
    
    
    
 
    user_q = st.text_input(label = 'Ask me below and I\'ll try my best to answer!')
    ans = st.empty()
    inf = st.empty()
    
    st.markdown('\n\n')
    
    imgs = utils.load_images()
    r = random.randint(0,16)
    
    st.image(imgs[r], use_column_width=True, caption = 'Photos sourced from unsplash.com vegan collection')
    
    
    df = utils.load_data()
    model = utils.load_model()
    
    if user_q == '':
        pass
    
    elif len(user_q.split())  < 3:
        st.info('Your question must be more than 3 words')
    
    else:
        with st.spinner('Loading Answer'):
            prediction = utils.comp_q(user_q, df, model)
            
            if prediction[0] >= 0.5:
                
                ans.success(
                        ':mag: \n**Answer:**\n' + prediction[2].reset_index(drop=True)[0])
                inf.info('Corpora Question: ' + prediction[1] + '\n\nSimilarity Score = ' + str(prediction[0]))
            else:
                ans.warning('Sorry I\'m not confident I can answer that correctly, please try another question')
            
        

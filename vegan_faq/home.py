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
    
    img = utils.get_image_url()
    caption = 'Photo by [' + img[1] + ']('+ img[2] + ') on [Unsplash](https://www.unsplash.com)' 
    
    st.image(img[0], use_column_width=True)
    st.markdown(caption)
    
    
    df = utils.load_data()
    model = utils.load_model()
    
    st.markdown(
    """
    ***
    # About
    ## What is SEV?
    **SEV** ( The 'Suprisingly Educated VeganBot') is a question-answering bot that tries to answer your *veganism related* questions!
    
    
    ## How does SEV work?    
    SEV tries to match your question to its stored knowledge bank - and then return the most relevant response.
    SEV is a 'closed domain' QA bot, and thus if the answer is not found in one of SEV's corpora, he will have a hard time answering
    the question!

    
    ## Tell me more about SEV's knowledge bank    
    SEV's knowledge bank was curated from various sources such as: reddit, wikipedia, bbc news, & vegan related websites.
    The set of questions & answers is quality controlled to ensure the responses accurately represent veganism!
    
    ***
    
    [![github][1]][2]
    [![email][3]][4]
     ![version][5]
    
    [1]:  https://img.shields.io/static/v1?label=github&message=vegan_faq&color=informational&logo=github
    [2]:  https://www.github.com/ME-64/vegan_faq
    [3]:  https://img.shields.io/static/v1?label=contact&message=miloelliott64@gmail.com&color=green&logo=gmail
    [4]:  mailto:miloelliott64@gmail.com
    [5]:  https://img.shields.io/static/v1?label=version&message=Proof%20of%20Concept&color=red
    
    """
    
    
    )
    
    if user_q == '':
        pass
    
    elif len(user_q.split())  < 3:
        ans.info('Your question must be more than 3 words')
    
    else:
        with st.spinner('Loading Answer'):
            prediction = utils.comp_q(user_q, df, model)
            
            if prediction[0] >= 0.5:
                
                ans.success(
                        ':mag: \n**Answer:**\n' + prediction[2].reset_index(drop=True)[0])
                inf.info('Corpora Question: ' + prediction[1] + '\n\nSimilarity Score = ' + str(prediction[0]))
            else:
                ans.warning('Sorry I\'m not confident I can answer that correctly, please try another question')
            
        

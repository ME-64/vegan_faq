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
    caption = 'Photo by [' + img[1] + ']('+ img[2] + ') on [Unsplash](https://www.unsplash.com)' + \
    ' - randomly selected from the vegan collection'
    
    st.image(img[0], use_column_width=True)
    st.markdown(caption)
    
    
    df = utils.load_data()
    model = utils.load_model()
    
    st.markdown(
    """
    ***
    # About
    ## What is VIRA?
    **VIRA** ('Vegan Information Retrieval Assistant') is a bot that tries to answer your
    *veganism related* questions!
    
    
    ## How does VIRA work?    
    VIRA tries to match your question to its stored knowledge bank - and then return
    the most relevant response.
    VIRA is a 'closed domain' QA bot, and thus if the answer is not found in one of 
    VIRA's corpora, he will have a hard time answering the question!

    
    ## Tell me more about VIRA's knowledge bank    
    VIRA's knowledge bank was curated from various sources such as: reddit, wikipedia,
    bbc news, & vegan related websites.
    The set of questions & answers is quality controlled to ensure the responses 
    accurately represent veganism!
    
    ## Tell me more about VIRA's information retrieval algorithm
    VIRA utilises a 'Universal Sentence Encoding' algorithm, trained on millions of sentences
    to try understand the semantics of a question.VIRA will  then find the best match between
    your question and a question in it's knowledge bank.

    Stay tuned for a full article on this approach and why this algorithm was used!

    ***
    
    [![github][1]][2]
    [![email][3]][4]
     ![version][5]
    
    [1]:  https://img.shields.io/static/v1?label=github&message=SEV&color=informational&logo=github
    [2]:  https://www.github.com/ME-64/vegan_faq
    [3]:  https://img.shields.io/static/v1?label=contact&message=miloelliott64@gmail.com&color=green&logo=gmail
    [4]:  mailto:miloelliott64@gmail.com
    [5]:  https://img.shields.io/static/v1?label=version&message=Protoype&color=red
    
    """
    
    
    )
    
    if user_q == '':
        ans.info('Here\'s some questions to get you started!\n'
                 ' - What makes people go vegan?\n'
                 ' - Do plants feel pain?\n'
                 ' - What is moral veganism?\n'
                 ' - Can vegans eat honey?\n'
                )
    
    elif len(user_q.split())  < 3:
        ans.info(':broken_heart: Your question must be more than 3 words')
    
    else:
        with st.spinner('Loading Answer'):
            prediction = utils.comp_q(user_q, df, model)
            
            if prediction[0] >= 0.5:
                know_bank = '\n\n *Associated question in my knowledge bank: *\n\n > ' + \
                            prediction[1]
                ans.success(
                        ':mag: \n**Answer:**\n' + prediction[2].reset_index(drop=True)[0])
               
                if prediction[0] <= 0.70:
                    inf.info('I think this might answer your question! :neutral_face:' + \
                            know_bank)
                elif prediction[0] <= 0.85:
                    inf.info('I\'m fairly confident this answers your question :grinning: :heavy_check_mark:' + \
                            know_bank)
                else:
                    inf.info('This looks like it answers your question perfectly!  :white_check_mark: :tada:' + \
                            know_bank)
            else:
                ans.warning(':disappointed: Sorry I\'m not confident I can answer that correctly, please try another question')
            
        

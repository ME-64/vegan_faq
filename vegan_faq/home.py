import time
import os
import random

import streamlit as st

import utils


def Home():
    """Home page"""
    
    st.subheader('Have a question about veganism:question:')
    user_q = st.text_input(label = 'Ask me below and I\'ll try my best to answer!')
    ans = st.empty()
    inf = st.empty()

    st.markdown('\n\n')

    try: 
        img = utils.get_image_url()

        caption = 'Photo by [' + img[1] + ']('+ img[2] + \
        ''') on [Unsplash](https://www.unsplash.com) - randomly selected from the 
        vegan collection'''

        st.image(img[0], use_column_width=True)
        st.markdown(caption)

    except:
        st.markdown(':confused: unsplash hourly API limit reached.' 
                'Come back later for more beautiful pictures!')


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
    VIRA's corpora, she will have a hard time answering the question!


    ## Tell me more about VIRA's knowledge bank    
    VIRA's knowledge bank was curated from various sources such as: reddit, wikipedia,
    bbc news, & vegan related websites.
    The set of questions & answers is quality controlled to ensure the responses 
    accurately represent veganism!

    Currently VIRA's knowledge bank is small, and thus she won't always be able to 
    assist. It is however being continually updated!

    ## Tell me more about VIRA's information retrieval algorithm
    VIRA utilises a 'Universal Sentence Encoder' algorithm. This approach was publicised 
    by google in [this](https://arxiv.org/abs/1803.11175) paper. Compared to traditional
    methods such as word2vec or glove - which create word embeddings, Universal Sentence
    Encoder creates 512 dimensional embeddings at the sentence level. VIRA will compare 
    the embeddings of your question, with those of the questions in her knowledge 
    bank - and then if there is a close enough match - retrive the answer!

    Stay tuned for a full article on this approach, including what could be improved,
    and why this algorithm was used over others!

    ***

    [![github][1]][2]
    [![email][3]][4]
     ![version][5]

    [1]:  https://img.shields.io/static/v1?label=github&message=VIRA&color=informational&logo=github
    [2]:  https://www.github.com/ME-64/VIRA
    [3]:  https://img.shields.io/static/v1?label=contact&message=miloelliott64@gmail.com&color=green&logo=gmail
    [4]:  mailto:miloelliott64@gmail.com
    [5]:  https://img.shields.io/static/v1?label=version&message=Protoype&color=red

    """


    )



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



    rand_questions = utils.select_random_questions(suggested_questions)


    if user_q == '':
        ans.info('Here\'s some questions to get you started!' + '\n - ' +  \
                rand_questions[0]  + '\n- '+ \
                rand_questions[1]  + '\n- '+ \
                rand_questions[2]   + '\n- '+ \
                rand_questions[3]
                )

    elif len(user_q.split())  < 3:
        ans.info(':broken_heart: Your question must be more than 3 words' + \
                 '\n\n Maybe try this question -  ' + random.choice(suggested_questions))

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
                    inf.info('I\'m fairly confident this answers your question' 
                            ':grinning: :heavy_check_mark:' + know_bank)
                else:
                    inf.info('This looks like it answers your question perfectly!'  
                    ':white_check_mark: :tada:' + know_bank)
            else:
                ans.warning(':disappointed: Sorry I\'m not confident I can answer' 
                        'that correctly, please try another question')
            
    

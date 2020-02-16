import streamlit as st


def About():
    st.markdown(
    """
    ***
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
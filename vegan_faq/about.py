import streamlit as st


def About():
    st.markdown(
    """
    ***
    ## What is SEV?
    **SEV** ( The 'Suprisingly Educated Vegan Bot') that tries to answer your *veganism related* questions!
    
    
    ## How does SEV work?    
    SEV tries to match your question to a store of collected questions and answers - and then treturn the most relevant response.
    SEV is a closed domain Q-A bot, and thus if the answer is not found in one of SEV's corpora, he will have a hard time answering
    the question!

    
    ## Tell me more about SEV's knowledge bank    
    SEV's knowledge bank was curated from various sources such as: reddit, wikipedia, bbc news, & vegan related websites.
    The set of questions & answers is quality controlled to ensure the responses accurately represent veganism!
    

    """
    
    
    )
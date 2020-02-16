import streamlit as st
import time
import pandas as pd
import os
import tensorflow as tf
import numpy as np
import pandas as pd
import utils
from home import Home
from about import About



#navigation = st.empty()
st.title(
''':recycle: :recycle: :recycle: :recycle: :recycle: :recycle: :recycle: :recycle: :recycle: :recycle: :recycle: :recycle: :recycle: :recycle: '''
)

st.title('The **S**uprisingly **E**ducated **V**eganBot')

navigation = st.sidebar.selectbox('Navigation:', ('Home', 'About'))


if navigation == 'Home':
    Home()
    
elif navigation == 'About':
    About()



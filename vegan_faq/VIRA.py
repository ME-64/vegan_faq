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


st.image('vegan_faq/static/vira_logo.png', use_column_width = True)

#navigation = st.sidebar.selectbox('Navigation:', ('Home', 'About'))
# removing navigation feature until streamlit handles it better on mobile
navigation = 'Home'

if navigation == 'Home':
    Home()
    
elif navigation == 'About':
    About()



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

navigation = st.selectbox('Navigation:', ('Home', 'About'))
st.markdown('## ***The Suprisingly* Educated Vegan Bot** :green_book:')


if navigation == 'Home':
    Home()
    
elif navigation == 'About':
    About()


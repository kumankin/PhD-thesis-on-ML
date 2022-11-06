from datetime import date, datetime

import streamlit as st
import pandas as pd
import os

with st.sidebar:
    st.title('AutoML')
    # st.sidebar.info(
    #         '''
    #         This application is an example of a machine learning pipeline.
    #         '''
    #     )
    choice = st.radio('Navigation', ['Introduction', 'Upload', 'EDA', 'ML'])
    
if choice == 'Introduction':
    pass

if choice == 'Upload':
    file = st.file_uploader('Upload Your data')

if choice == 'EDA':
    pass

if choice == 'ML':
    pass
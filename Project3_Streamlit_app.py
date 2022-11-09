import pandas as pd
import streamlit as st
import pickle
from PIL import Image

#Page configuration
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

#Background image:

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('./Picture1.jpg')


#Define columns:
col1, col2, col3 = st.columns(3)

with col1:
    ('')
    
with col2:
    st.markdown("<h1 style='text-align: center; color: White;'>InovMovie</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: Steelblue;'>The best app for movie theatres</h1>", unsafe_allow_html=True)
    
    selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
     movies['title'].values
    )

    
    
with col3:
    ('')
    
    session.options = st.multiselect(label="Select Movies", options=movies)

    

    
#     session.slider_count = st.slider(label="movie_count", min_value=5, max_value=50)

#     st.text("")
#     st.text("")

#     buffer1, col1, buffer2 = st.columns([1.45, 1, 1])

#     is_clicked = col1.button(label="Recommend")

#     if is_clicked:
#     dataframe = recommend_table(session.options, movie_count=session.slider_count, tfidf_data=tfidf)

#     st.text("")
#     st.text("")
#     st.text("")
#     st.text("")

#     if dataframe is not None:
#         st.table(dataframe)
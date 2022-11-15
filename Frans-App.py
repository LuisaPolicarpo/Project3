### Imports
import streamlit as st
import pandas as pd
import numpy as np  
import re
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import SnowballStemmer
from string import punctuation
from wordcloud import WordCloud
import pickle
from PIL import Image
import requests
import streamlit_nested_layout

###Import Data
reviews_wc = pd.read_pickle("pickles/review_final-wc_p.pkl")

### Define columns:
st.set_page_config(page_title=None, page_icon=None, layout="wide", menu_items=None)
# col1, col2, col3 = st.columns([2,1,1])

# with col1:
#     title = st.text_input('Type the title and press Enter')
# if title:
#         try: 
#             url = f"https://www.omdbapi.com/?t={title}&apikey=38187759"
#             re = requests.get(url)
#             re = re.json()
#             col1, col2, = st.columns([1,1])
#             with col1:
#                     st.image(re['Poster'])
#             with col2:
#                     st.subheader(re['Title'])
#                     st.caption(f"Gender:{re['Genre']} Year: {re['Year']} ")
#                     st.write (re['Plot'])
#                     st.text(f"Rating: {re['imdbRating']}")
#                     st.progress(float(re['imdbRating'])/10)
#         except:
#                 title = False
#                 st.error('We currently don'')
#                 contact_form = """
#     <form action="https://formsubmit.co/inovmovie@gmail.com" method="POST">
#      <input type="text" name="Suggestion" placeholder="Movie suggestion" required>
#      <input type="text name="Name" placeholder="Your name" required>
#      <button type="submit">Send</button>
# </form>
# """
#                 st.markdown (contact_form, unsafe_allow_html=True)

# with col2:
#     st.markdown('hola')

# with col3:
#     st.title('hola')

outer_cols = st.columns([2,1,2])

with outer_cols[0]:
    st.markdown('## Column 1')
    st.selectbox('selectbox', [1,2,3], key='sel1')
    
    inner_cols = st.columns([1,1])
    with inner_cols[0]:
        st.markdown('Nested Column 1')
        st.selectbox('selectbox', [1,2,3], key='sel2')
    with inner_cols[1]:
        st.markdown('Nested Column 2')
        st.selectbox('selectbox', [1,2,3], key='sel3')

with outer_cols[1]:
    st.markdown('')
    
with outer_cols[2]:
    st.markdown('## Recommendations')
    inner_cols = st.columns([1])
    with inner_cols[0]:
        st.markdown('Recomended 1')
        st.selectbox('selectbox', [1,2,3], key='t2')
    with inner_cols[0]:
        st.markdown('Recomended 2')
        st.selectbox('selectbox', [1,2,3], key='t1')
    with inner_cols[0]:
        st.markdown('Recomended 3')
        st.selectbox('selectbox', [1,2,3], key='t3')
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
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split

### Import Data
reviews_wc = pd.read_pickle("pickles/review_final-wc_p.pkl")

### Page configuration
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

### Background image:
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


### Define columns:
col1, col2, col3 = st.columns(3)

with col1:
    genre_input = st.selectbox('Type a genre: ')
    st.write('This is a re the most recurring words to describe ', genre_input, ' genre')
    
    ### Word Cloud for Genre with str contains
    select_genre = str(input('Type :'))
    text03 = reviews_wc[reviews_wc['genres'].str.contains(genre_input, na=False)]['review_content']
    text03 = str(text03)
    text03 = re.sub(r"\d+","",text03)
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    nopunc = tokenizer.tokenize(text03)
    words03=" ".join(nopunc)
    words03= nltk.word_tokenize(words03.lower())
    x3 = re.findall("[0-9]+",text03)
    stop_words = set(stopwords.words('english'))
    stop_words |= set(x3) #add the list with all the numbers in the string to the list of stopwords
    stop_words.update({'n', 'name', 'review_content','length', 'dtype', 'object','movie','film','films','th','one','like','sharknado','b',genre_input.lower()})
    words = words03

    sentence04 = [w for w in words if not w in stop_words]

    wordcloud = WordCloud(width=200, height=200,background_color='white', max_font_size=200, min_font_size=10, max_words=10)

    sentence1 = sentence04
    freq = nltk.FreqDist(sentence1)

    wordcloud.generate_from_frequencies(freq)

    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()
    
with col2:
    st.markdown("<h1 style='text-align: center; color: White;'>InovMovie</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: Steelblue;'>The best app for movie theatres</h1>", unsafe_allow_html=True)
    
    #Import table
    # df_inovmovie = pd.read_pickle('/content/drive/MyDrive/Colab Notebooks/Projects/Project3_my copy/title_basics_p.pkl')
    # movie_list = df['PrimaryTitle'].tolist()
    d = {'col1': ['Marta', 'Luísa', 'Frans'], 'col2': [3, 4, 5]}
    df = pd.DataFrame(data=d)
    # col1_list = df['col1'].tolist()
    # col1_list = [1, 2, 3]
    
    #Selectbox for movie names
    text_input = st.selectbox('Movie title', df['col1'])
    # text_input = st.text_input('Movie title', autocomplete= df['col1'])  

    if text_input:
        st.write("You entered: ", text_input)
        
#Luisa

    
    #Button to run
    # pickle.dump(xxx,open('xxxx.pkl','wb'))
    
    #KNN distance model

    
    
    
    
with col3:
    ('')
    # session.options = st.multiselect(label="Select Movies", options=movies)
    
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

    # text_input = st.text_input(
    #         "Enter some text 👇",
    #         label_visibility=st.session_state.visibility,
    #         disabled=st.session_state.disabled,
    #         placeholder=st.session_state.placeholder,
    #     )



    #  selected_movie_name = st.selectbox('Select', movie_list)
    # selected_movie_name = st.selectbox(
    # "Type or select a movie from the dropdown",
    #  df_inovmovie['PrimaryTitle'].values
    # )
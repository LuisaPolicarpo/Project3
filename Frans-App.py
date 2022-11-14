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

###Import Data
reviews_wc = pd.read_pickle("pickles/review_final-wc_p.pkl")

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
    ('')

with col3:
    selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    reviews_wc['movie_title'].values)
      
### Imports
import streamlit as st
import pandas as pd
import numpy as np  
import re
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from string import punctuation
import pickle
from PIL import Image
import requests
import streamlit_nested_layout
from streamlit_option_menu import option_menu

from sklearn.neighbors import NearestNeighbors

##GLOBAL VARIABLES
###Import Data
df_inovmovie = pd.read_pickle("D:\Wild Code School\Project3\Project 3\Table for the app\condition_gi.pickle")

###Columns to recommend
recommendation_columns = ['startYear', 'wheighted_IMDB',
           'Action', 'Adult', 'Adventure', 'Animation',
           'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
           'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music',
           'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi',
           'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']

###create df without the movie we want to recommend
df_inovmovie_nf = df_inovmovie_n[df_inovmovie_n['primaryTitle'].str.contains(name) == False]

###call the model and fit to variables
model = NearestNeighbors(n_neighbors=5).fit(X1)

##PRE-PROCESSING
df_inovmovie = df_inovmovie.drop(['tconst','\\N'], axis = 1)
df_inovmovie_n = df_inovmovie.dropna(subset=['wheighted_IMDB'])



# Libraries dividing in groups
# global variables Ex. recommendation columns
# functions (def rec)
# pre-processing (model_fit)

##SHOW WITH STREAMLIT
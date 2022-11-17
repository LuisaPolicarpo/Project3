### Imports
import streamlit as st
import pandas as pd
import numpy as np  
import re
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from sklearn.neighbors import NearestNeighbors
from string import punctuation
import pickle
from PIL import Image
import requests
import streamlit_nested_layout
from streamlit_option_menu import option_menu

### Load Data
movies = pd.read_pickle("C:\\Users\\frans\\Documents\\GitHub\\Fork-P3\\pickles\\condition_gi.pickle")

### Prepare data
movies.drop(['tconst','\\N'], axis = 1, inplace = True)
movies_n = movies.dropna(subset=['wheighted_IMDB'])

### Global Variables
recommendation_columns = ['startYear', 'wheighted_IMDB',
           'Action', 'Adult', 'Adventure', 'Animation',
           'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
           'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music',
           'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi',
           'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']

### Model 
X1 = movies_n[recommendation_columns]
model = NearestNeighbors(n_neighbors=5).fit(X1)

### Functions
def rec(name, model):
        df_inovmovie_nf = movies_n[movies_n['primaryTitle'].str.contains(name) == False] 
        test = movies_n.loc[movies_n['primaryTitle'].isin([name]), recommendation_columns]

        array1, array2 = model.kneighbors(test)

        list_1 = array1.tolist()
        list_2 = array2.tolist()

        flat_list1 = list(np.concatenate(list_1).flat)
        flat_list2 = list(np.concatenate(list_2).flat)

        d = {'Distance': flat_list1,'index': flat_list2}
        df12 = pd.DataFrame(d)

        dfnl_df12 = pd.merge(df_inovmovie_nf, df12, how='inner', on=["index", "index"])
      
        return dfnl_df12.sort_values(by = 'Distance').iloc[1:4, 'primaryTitle']

### Streamlit
name1 = st.text_input('Enter a movie')
rec(name = name1,model = model)
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

###Import Data
df_inovmovie = pd.read_pickle("D:\Wild Code School\Project3\Project 3\Table for the app\condition_gi.pickle")
df_inovmovie = df_inovmovie.drop(['tconst','\\N'], axis = 1)
df_inovmovie_n = df_inovmovie.dropna(subset=['wheighted_IMDB'])

recommendation_columns = ['startYear', 'wheighted_IMDB',
           'Action', 'Adult', 'Adventure', 'Animation',
           'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
           'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music',
           'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi',
           'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']

### Define columns:
st.set_page_config(page_title=None, page_icon="🎥", layout="wide", menu_items=None)

tab1, tab2, tab3 = st.tabs(["Inov Movie", "Recomendations", "Top Movies"])

with tab1:
    
    st.header("Inov Movie")
    ##Remove the movie that is to be recomended from the list
    name = ('Pulp Fiction')

    df_inovmovie_nf = df_inovmovie_n[df_inovmovie_n['primaryTitle'].str.contains(name) == False]
    # condition_gi_nn = condition_gi.loc[condition_gi['primaryTitle'] != name]

    name1 = ['Pulp Fiction']

    X1 = df_inovmovie_n[recommendation_columns]


    model = NearestNeighbors(n_neighbors=5).fit(X1)
    
    test = df_inovmovie_n.loc[df_inovmovie_n['primaryTitle'].isin(name1), recommendation_columns]
    st.table(test)
    
    array = model.kneighbors(test)
    st.write(array)

    # array1, array2 = model.kneighbors(df_inovmovie_n.loc[df_inovmovie_n['primaryTitle'].isin(name1), ['startYear', 'wheighted_IMDB',
    #        'Action', 'Adult', 'Adventure', 'Animation',
    #        'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
    #        'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music',
    #        'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi',
    #        'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']])

    list_1 = array1.tolist()
    list_2 = array2.tolist()

    flat_list1 = list(np.concatenate(list_1).flat)
    flat_list2 = list(np.concatenate(list_2).flat)

    d = {'Distance': flat_list1,'index': flat_list2}
    df12 = pd.DataFrame(d)
    df12

    dfnl_df12 = pd.merge(df_inovmovie_nf, df12, how='inner', on=["index", "index"])
    dfnl_df12.sort_values(by = 'Distance').head(5)
    # title_rec = list(dfnl_df12_sort['primaryTitle'])
    # title_rec1 = title_rec[0]
    # title_rec1 = title_rec[1]
    # title_rec1 = title_rec[2]

    
with tab2:    
 outer_cols = st.columns([2,0.5,2])

### Left side of screen
with outer_cols[0]:
    st.markdown('## Movie')
    title = st.text_input('Type the title and press Enter')
    
       

    if title:
            try: 
                url = f"https://www.omdbapi.com/?t={title}&apikey=38187759"
                re = requests.get(url)
                re = re.json()

                inner_cols = st.columns([1,2])
                with inner_cols[0]:
                    st.image(re['Poster'])

                with inner_cols[1]:
                    st.header(re['Title'])
                    st.caption(f"Gender:{re['Genre']} Year: {re['Year']} ")
                    st.write (re['Plot'])
                    st.text(f"Rating: {re['imdbRating']}")
                    st.progress(float(re['imdbRating'])/10)

                        ### Right side of screen    
                    with outer_cols[0]:
                        st.markdown('')
                        
                    with outer_cols[2]:
                        st.markdown('## Recommendations')
                        inner_cols = st.columns([1,2])
                        
                        with inner_cols[0]:
                            st.image(re['Poster'], width=125)
                        
                        with inner_cols[1]:
                            st.subheader(re['Title'])
                            st.write (re['Plot'])
                            st.text(f"Rating: {re['imdbRating']}")
                        
                        inner_cols = st.columns([1,2])
                        with inner_cols[0]:
                            st.image(re['Poster'], width=125)
                        with inner_cols[1]:
                            st.subheader(re['Title'])
                            st.write (re['Plot'])
                            st.text(f"Rating: {re['imdbRating']}")
                        
                        inner_cols = st.columns([1,2])
                        with inner_cols[0]:
                            st.image(re['Poster'], width=125)
                        with inner_cols[1]:
                            st.subheader(re['Title'])
                            st.write (re['Plot'])
                            st.text(f"Rating: {re['imdbRating']}")

            except:
                title = False
                st.markdown('''We currently don't have detailed information on this movie
                drop us an email and our scouting team will look into it and will send you our review''')
                contact_form = """
                <form action="https://formsubmit.co/inovmovie@gmail.com" method="POST">
                <input type="text" name="Suggestion" placeholder="Movie suggestion" required>
                <input type="text name="Name" placeholder="Your name" required>
                <button type="submit">Send</button>
                </form>
                """
                st.markdown (contact_form, unsafe_allow_html=True)
with tab3:
   st.header("Check the movies that everybody loves")
   col, col1, col2 = st.columns(3)
   col3, col4, col5 = st.columns(3)
   col6, col7, col8 = st.columns(3)
with col:
   st.video("https://www.youtube.com/watch?v=6hB3S9bIaco")
with col1:
   st.video("https://www.youtube.com/watch?v=sY1S34973zA")
with col2:
   st.video("https://www.youtube.com/watch?v=EXeTwQWrcwY")
with col3:    
   st.video("https://www.youtube.com/watch?v=r5X-hFf6Bwo")
with col4:
   st.video("https://www.youtube.com/watch?v=gG22XNhtnoY")
with col5:
   st.video("https://www.youtube.com/watch?v=OA1ij0alE0w")
with col6:
  st.video("https://www.youtube.com/watch?v=_13J_9B5jEk")
with col7: 
  st.video("https://www.youtube.com/watch?v=tGpTpVyI_OQ")
with col8:
  st.video("https://www.youtube.com/watch?v=8hP9D6kZseM")


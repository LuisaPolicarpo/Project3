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


###name test
# movie_name = 'Pulp Fiction'

##PRE-PROCESSING
###clean data
df_inovmovie = df_inovmovie.drop(['tconst','\\N'], axis = 1)
df_inovmovie_n = df_inovmovie.dropna(subset=['wheighted_IMDB'])

X1 = df_inovmovie_n[recommendation_columns]

###call the model and fit to variables
nn_alg = NearestNeighbors(n_neighbors=5).fit(X1)


##FUNCTIONS

def rec(name, model):
    
        test = df_inovmovie_n.loc[df_inovmovie_n['primaryTitle'].isin([name]), recommendation_columns]

        array1, array2 = model.kneighbors(test)

        list_1 = array1.tolist()
        list_2 = array2.tolist()

        flat_list1 = list(np.concatenate(list_1).flat)
        flat_list2 = list(np.concatenate(list_2).flat)

        d = {'Distance': flat_list1,'index': flat_list2}
        
        df12 = pd.DataFrame(d)
        
        df_inovmovie_nf = df_inovmovie[df_inovmovie['primaryTitle'].str.contains(name) == False]

        dfnl_df12 = pd.merge(df_inovmovie_nf, df12, how='inner', on=["index", "index"])
        
        return dfnl_df12.sort_values(by = 'Distance').iloc[1:4]['primaryTitle']


# Libraries dividing in groups
# global variables Ex. recommendation columns
# functions (def rec)
# pre-processing (model_fit)

##SHOW WITH STREAMLIT

# movie_name = st.selectbox(
#     'Select a movie',
#     list(df_inovmovie_n['primaryTitle']))

# if movie_name:
#     test = rec(movie_name, nn_alg)
#     st.table(test)

st.set_page_config(page_title="Inov Movie", page_icon="🎥", layout="wide", menu_items=None)

tab1, tab2 = st.tabs(["Recomendations", "Top Movies"])


with tab1:
        outer_cols = st.columns([2,0.5,2])
        st.header("Inov Movie")
        title = st.selectbox('Select a movie', df_inovmovie['primaryTitle'])


        with outer_cols[0]:
                if title:
                        title_rec = rec(title, nn_alg)

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
                                ### Recomendation outputs
                        with outer_cols[2]:
                                st.markdown('## Recommendations')
                        
                        inner_cols = st.columns([1,2])
                        with inner_cols[0]:
                                url = f"https://www.omdbapi.com/?t={title_rec[0]}&apikey=38187759"
                                re = requests.get(url)
                                re = re.json()
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
                              #Recommednation engine
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
   #  selected = option_menu(
   #  menu_title="In case of lack of ideias", 
   #  options = ["Drama", "Romance", "Comedy"],
   #  orientation = "horizontal",)
   # # st.header("Our main Sucess")
   #  # tab1, tab2 = st.tabs(["📈 Recomendation", "🗃 Top movies"])
   #  if selected == "Drama":
   #      tab1.subheader("A tab with a chart")
    col, col1, col2 = st.columns(3)


    with col:
        st.subheader('The Shawshank Redemption')
        st.markdown('**_Gender_**: Drama')
        st.markdown('**_Year_**: 1994')
   # st.text('Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.')
        st.video("https://www.youtube.com/watch?v=6hB3S9bIaco")

    with col1:
        st.subheader('The Godfather')
        st.markdown('**_Gender_**: Crime')
        st.markdown('**_Year_**: 1972')
   # st.text('The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son')
        st.video("https://www.youtube.com/watch?v=sY1S34973zA")
    with col2:
        st.subheader('The Dark Knight')
        st.markdown('**_Gender_**: Action, Crime, Drama')
        st.markdown('**_Year_**: 2008')
   # st.text('When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.')
        st.video("https://www.youtube.com/watch?v=EXeTwQWrcwY")
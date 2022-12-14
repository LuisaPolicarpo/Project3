### Imports
import streamlit as st
import pandas as pd
import numpy as np  
import re
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
<<<<<<< Updated upstream
=======
import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import SnowballStemmer
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
>>>>>>> Stashed changes
from string import punctuation
import pickle
from PIL import Image
import requests
import streamlit_nested_layout
from streamlit_option_menu import option_menu
from sklearn.neighbors import NearestNeighbors
# server.maxMessageSize
###Import Data
#reviews_wc = pd.read_pickle("pickles/review_final-wc_p.pkl")
<<<<<<< Updated upstream
movies = pd.read_pickle("C:\\Users\\frans\\Documents\\GitHub\\Fork-P3\\pickles\\condition_gi.pickle")
movies.drop(['tconst','\\N'], axis = 1, inplace = True)

=======
st.set_page_config(page_title="Inov Movie", page_icon="🎥", layout="wide", menu_items=None)
movies = pd.read_pickle("C:/Users/luisa/OneDrive/Documentos/GitHub/Project3/condition_gi.pickle")
# st.table(movies.head())
movies.drop(['tconst','\\N'], axis = 1, inplace = True)
st.table(movies.head())
# input 
>>>>>>> Stashed changes
### Define columns:

tab2, tab3 = st.tabs([ "Recomendations", "Top Movies"])

# with tab1:
    
<<<<<<< Updated upstream
    st.header("Inov Movie")
    st.table(movies.head(10))
=======
#     st.header("Inov Movie")
#    #st.image(image4, width=1000) 
>>>>>>> Stashed changes

    
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

#     if selected == "Romance":
#          col3, col4, col5 = st.columns(3)
#     with col3:    
#         st.video("https://www.youtube.com/watch?v=r5X-hFf6Bwo")
#     with col4:
#         st.video("https://www.youtube.com/watch?v=gG22XNhtnoY")
#     with col5:
#         st.video("https://www.youtube.com/watch?v=OA1ij0alE0w")

#     if selected == "Comedy":
#          col6, col7, col8 = st.columns(3)
#     with col6:
#         st.video("https://www.youtube.com/watch?v=_13J_9B5jEk")
#     with col7: 
#         st.video("https://www.youtube.com/watch?v=tGpTpVyI_OQ")
#     with col8:
#         st.video("https://www.youtube.com/watch?v=8hP9D6kZseM")


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
df_inovmovie = pd.read_pickle("C:/Users/luisa/OneDrive/Documentos/GitHub/Project3/condition_gi.pickle")
df_inovmovie = df_inovmovie.drop(['tconst','\\N'], axis = 1)
df_inovmovie_n = df_inovmovie.dropna(subset=['wheighted_IMDB'])

X  = ['startYear', 'wheighted_IMDB',
           'Action', 'Adult', 'Adventure', 'Animation',
           'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
           'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music',
           'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi',
           'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']

### Define columns:

    

#     name = 'Pulp Fiction'

#     df_inovmovie_nf = df_inovmovie_n[df_inovmovie_n['primaryTitle'].str.contains(name) == False]
#     # condition_gi_nn = condition_gi.loc[condition_gi['primaryTitle'] != name]

#     # name1 = ['Pulp Fiction']

#     X1 = df_inovmovie_n[recommendation_columns]
    
model = NearestNeighbors(n_neighbors=5).fit(X).reshape(1, -1)
    
user_input = st.text_input("Tell us a movie so we can show you some recommendations: ")

input_results = movies[movies['primaryTitle'].str.contains(user_input, na = False)]['primaryTitle']
    
options = st.multiselect('Please choose one film from below:', input_results)

clean_option = str(options)
cleaner_option = clean_option[2:-2]    
if st.button('Submit'):
    movie = movies.loc[movies.primaryTitle == cleaner_option]
    movie_index = movie.index.astype(int)
    favorite = list(X.iloc[movie_index[0]])

    prediction = distanceKNN.kneighbors([favorite])
    results = prediction[1].tolist()
    results = results[0]
    results_n = movies.iloc[results]
    results_a = results_n[["primaryTitle","director"]]
    results_a.rename(columns={"primaryTitle": "Title:", "director" : "Directed by:"}, inplace = True)

    st.header("Thank you very much! Please check below what we have for you:")
    st.write(results_a[1:5])    
    
    
    
    
    
#     def rec(name, model):
    
#         test = df_inovmovie_n.loc[df_inovmovie_n['primaryTitle'].isin([name]), recommendation_columns]
#         # st.table(test)

#         array1, array2 = model.kneighbors(test)
#         # st.write(array)

#         # array1, array2 = model.kneighbors(df_inovmovie_n.loc[df_inovmovie_n['primaryTitle'].isin(name1), ['startYear', 'wheighted_IMDB',
#         #        'Action', 'Adult', 'Adventure', 'Animation',
#         #        'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family',
#         #        'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music',
#         #        'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi',
#         #        'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western']])

#         list_1 = array1.tolist()
#         list_2 = array2.tolist()

#         flat_list1 = list(np.concatenate(list_1).flat)
#         flat_list2 = list(np.concatenate(list_2).flat)

#         d = {'Distance': flat_list1,'index': flat_list2}
#         df12 = pd.DataFrame(d)

#         dfnl_df12 = pd.merge(df_inovmovie_nf, df12, how='inner', on=["index", "index"])
#         # dfnl_df12.sort_values(by = 'Distance').head(5)
#         return dfnl_df12.sort_values(by = 'Distance').iloc[1:4, 'primaryTitle'] #head(5))
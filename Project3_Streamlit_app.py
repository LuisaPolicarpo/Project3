import pandas as pd

# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split

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
      
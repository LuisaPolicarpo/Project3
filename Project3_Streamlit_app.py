import pandas as pd
import streamlit as st
import pickle

<<<<<<< HEAD

# <style>
# p {
#  background-image: url('./Picture1.JPG');
# }
# </style>

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("./Picture1.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("'./Picture1.JPG'");
#     background-size: cover;
#     }
#     </style>
#     '''
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return

# set_png_as_page_bg('background.png')

# st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('InovMovie')
=======
add_selectbox = st.sidebar.selectbox(
    "cat:",
    ["Cover","Frans", "Marta", "Luísa"])   

if add_selectbox == 'Cover':
    st.title('InovMovie')
    image = Image.open('C:/Users/luisa/OneDrive/Ambiente de Trabalho/WCS/Project 3/movie.jpg')
    st.image(image)
    
    st.subheader('A new solution that can change the movie industry')
>>>>>>> a5396416387ee0faec02d7412bc179720906b9c2

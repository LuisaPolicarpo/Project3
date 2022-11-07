import pandas as pd
import streamlit as st
import pickle

add_selectbox = st.sidebar.selectbox(
    "cat:",
    ["Cover","Frans", "Marta", "Luísa"])   

if add_selectbox == 'Cover':
    st.title('InovMovie')
    image = Image.open('C:/Users/luisa/OneDrive/Ambiente de Trabalho/WCS/Project 3/movie.jpg')
    st.image(image)
    
    st.subheader('A new solution that can change the movie industry')

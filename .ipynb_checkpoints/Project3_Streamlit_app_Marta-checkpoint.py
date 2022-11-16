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
      
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    # Fetch movie data from TMDb API
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US&api_key=1c9f3893b2f928a0c4cce9a192d11926")

    if response.status_code == 200:  # Check if the request was successful
        data = response.json()
        print(data)  # Debugging step to see the response

        # Check if 'poster_path' is present in the response
        if 'poster_path' in data:
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
        else:
            # Fallback URL when poster_path is missing
            return "https://via.placeholder.com/500x750?text=No+Poster+Available"
    else:
        # Handle the case where the API request fails
        return "https://via.placeholder.com/500x750?text=Error+Fetching+Poster"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]

    l = []
    l_post = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        l.append(movies.iloc[i[0]].title)
        l_post.append(fetch_poster(movie_id))
    return l, l_post

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommender System')

import streamlit as st

selected_movie_name = st.selectbox(
    "Enter your Preferences",
    movies['title'].values)


if st.button("Recommend Movies"):
    names,recc = recommend(selected_movie_name)

    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    # col9 = st.columns(1)

    with col1:
        st.text(names[0])
        st.image(recc[0])

    with col2:
        st.text(names[1])
        st.image(recc[1])

    with col3:
        st.text(names[2])
        st.image(recc[2])

    with col4:
        st.text(names[3])
        st.image(recc[3])

    with col5:
        st.text(names[4])
        st.image(recc[4])
    with col6:
        st.text(names[5])
        st.image(recc[5])
    with col7:
        st.text(names[6])
        st.image(recc[6])
    with col8:
        st.text(names[7])
        st.image(recc[7])
    # with col9:
    #     st.text(names[8])
    #     st.image(recc[8])

    # for i in recc:
    #     st.write(i)
    # streamlit run app.py


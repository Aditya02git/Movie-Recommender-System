import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_posters(movie_id):
    try:
        response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bbcd0722ada957489c457af24760fc36&language=en-US'.format(movie_id))
        data = response.json()
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500" + data['poster_path']
        else:
            return None
    except:
        return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    recommended_movie_ids = []
    
    for i in movies_list:
        # Get the actual movie ID from the DataFrame
        movie_id = movies.iloc[i[0]]['movie_id']  # Assuming there's a 'movie_id' column
        recommended_movie_ids.append(movie_id)
        recommended_movie_posters.append(fetch_posters(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies, recommended_movie_posters


# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

option = st.selectbox(
    'Select a movie:', movies['title'].values)

if st.button('Recommend'):
    st.write('You selected:', option)
    
    # Get recommendations and posters
    recommended_movies, recommended_posters = recommend(option)
    
    # Display recommendations
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    
    for i, col in enumerate(columns):
        with col:
            st.text(recommended_movies[i])
            if recommended_posters[i]:
                st.image(recommended_posters[i])
            else:
                st.text("No poster available")
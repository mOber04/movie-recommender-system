import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# 1. PAGE CONFIG: Sets the tab title and icon in your browser
st.set_page_config(page_title="Movie Matcher", page_icon="🎬", layout="wide")

# 2. CUSTOM CSS: Making it look "dark mode" and modern
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #e50914; /* Netflix Red */
        color: white;
    }
    .movie-title {
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        height: 3em;
    }
    </style>
    """, unsafe_allow_html=True)

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load Data
movies_dict = pickle.load(open(os.path.join(current_dir, 'movie_dict.pkl'), 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open(os.path.join(current_dir, 'similarity.pkl'), 'rb'))


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    try:
        data = requests.get(url).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    names, posters = [], []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return names, posters


# 3. VISUAL LAYOUT
st.title('🎬 Movie Matcher')
st.subheader('Find your next favorite film based on what you love.')

# Search Bar
selected_movie = st.selectbox("Search for a movie in our database:", movies['title'].values)

if st.button('Get Recommendations'):
    # A spinner makes the app feel responsive while fetching API data
    with st.spinner('Scanning the archives...'):
        names, posters = recommend(selected_movie)

        # Displaying recommendations in a neat grid
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(posters[i])
                # Using custom HTML class for consistent title heights
                st.markdown(f'<p class="movie-title">{names[i]}</p>', unsafe_allow_html=True)
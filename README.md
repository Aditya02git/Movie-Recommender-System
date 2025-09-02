# 🎬 Movie Recommender System

A **content-based movie recommender system** built with **Python, Streamlit, and TMDB API**.  
It suggests similar movies based on the one you select and displays their posters.

🔗 **Live Demo:** [Movie Recommender System](https://movie-recommender-system-1-8q99.onrender.com/)

---

## Features
-  Interactive **Streamlit** web app
-  Choose a movie and get **top 5 similar recommendations**
-  Fetches **movie posters** using [TMDB API](https://www.themoviedb.org/documentation/api)
-  Lightweight and easy to deploy on **Render / Heroku**

---

## Demo Preview
![Demo Screenshot](https://i.ibb.co/tscn58x/movie-recommender-demo.png)

---

## Tech Stack
- **Frontend/Backend**: [Streamlit](https://streamlit.io/)  
- **Data Handling**: Pandas, Pickle  
- **Similarity Computation**: Cosine Similarity / Precomputed Matrix  
- **API**: TMDB API for fetching movie posters  

---

## Installation & Setup

Clone the repository:
```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system

## Create & Activate a Virtual Environment

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

## Install dependecies

pip install -r requirements.txt

## Run app locally

streamlit run app.py


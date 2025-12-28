# 🎬 Movie Matcher: Content-Based Recommender

A machine learning web application that suggests movies based on content similarity. This project uses Natural Language Processing (NLP) to analyze movie metadata and provide high-quality recommendations.

## 🧠 How the Engine Works
The recommendation engine is built on two core concepts of data science:

1. **Vectorization:** I used `CountVectorizer` to convert text "tags" (genres, overviews, and keywords) into a 5,000-dimensional mathematical space.
2. **Cosine Similarity:** Instead of using Euclidean distance, the system calculates the "cosine" of the angle between vectors to find movies with the most similar content.

## 🛠️ Technology Stack
* **Language:** Python 3.12
* **Data Handling:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn
* **Web Framework:** Streamlit
* **API:** TMDB (The Movie Database)

## 💻 How to Run Locally
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Add your TMDB API Key to a `.env` file.
4. Run the command: `streamlit run main.py`

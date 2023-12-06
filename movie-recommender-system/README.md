

---

# Movie Recommender System

## Overview

The Movie Recommender System is a Python-based application that recommends movies based on user preferences. It utilizes the Streamlit framework for the user interface and employs collaborative filtering to generate movie recommendations.

## Features

- **User-Friendly Interface:** The Streamlit interface provides an intuitive and user-friendly experience for users to discover movie recommendations.

- **Collaborative Filtering:** The recommender system uses collaborative filtering techniques to suggest movies based on user preferences and similarities.

- **Movie Information:** Detailed information about movies, including posters, is fetched from The Movie Database (TMDb) API.

## Getting Started

### Prerequisites

Make sure you have the following dependencies installed:

```bash
pip install streamlit pandas scikit-learn requests
```

### Running the Application

1. Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Open the provided URL in your web browser to access the Movie Recommender System.

## Usage

1. Select a movie from the dropdown list or type the name of a movie.
2. Click the "Show Recommendation" button to view a list of recommended movies.
3. Explore the recommended movies with their titles and posters.

## Data Sources

- **Movie Data:** The movie details are sourced from the [TMDb API](https://www.themoviedb.org/documentation/api).

## Project Structure

- `app.py`: The main Streamlit application script.
- `requirements.txt`: Lists the Python packages required for the project.
- `movie_list.pkl`: Pickle file containing movie details.
- `similarity.pkl`: Pickle file containing similarity scores for movie recommendations.

## Future Enhancements

- Implement additional recommendation algorithms.
- Improve the user interface with more interactive features.
- Deploy the application to a web server for broader access.


## Acknowledgments

- [Streamlit](https://www.streamlit.io/) for providing an excellent framework for building data applications.
- [TMDb API](https://www.themoviedb.org/documentation/api) for supplying movie details.

---


# MovieNest-api

This project aims to develop an API that uses Django REST Framework and the TMDB API to provide movie recommendations to users. The API will also incorporate artificial intelligence techniques to improve the accuracy of the recommendations.

## Model Descriptions

### User Model
This model will represent the users of the API. The attributes may include:
- `username`
- `email`
- `password`
- `date_joined`

### Movie Model
This model represents the movies that will be recommended to users. Each `Movie` instance contains a variety of information about a specific movie. Here are the attributes of the `Movie` model:

- `tmdb_id`: The unique ID of the movie in TMDB.
- `title`: The title of the movie.
- `original_title`: The original title of the movie.
- `adult`: A boolean indicating whether the movie is for adults.
- `backdrop_path`: The path to the movie's backdrop.
- `genres`: The genres of the movie.
- `original_language`: The original language of the movie.
- `overview`: A synopsis of the movie.
- `popularity`: The popularity of the movie.
- `poster_path`: The path to the movie's poster.
- `release_date`: The release date of the movie.
- `video`: A boolean indicating whether the movie has a video.
- `vote_average`: The average rating of the movie.
- `vote_count`: The number of votes the movie has received.

## User Management

The API will provide functionalities for user management, including user account creation, user authentication, and updating user profile information.

## Movie Recommendations

The movie's synopsis (`overview`) can be used to generate movie recommendations. You could use natural language processing (NLP) techniques to analyze the synopses and determine the similarity between different movies. Then, you could recommend movies that are similar to those the user has positively rated in the past.
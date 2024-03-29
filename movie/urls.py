from django.urls import include, path
from . import views
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('new_movies', views.movies, name='movies'),
    #http://localhost:8000/movies/new_movies
    path('genre/<int:genre_id>', views.movies_by_genre, name='movies_by_genre'),
    #http://localhost:8000/movies/genre/28
    path('video/<int:movie_id>', views.movie_video, name='movie_video'),
    #http://localhost:8000/movies/video/1011985
    path('<int:movie_id>/genres/', views.get_movie_genres, name='movie-genres'),
    #http://localhost:8000/movies/1011985/genres
]
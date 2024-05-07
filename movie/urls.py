from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.MovieViewSet)
router.register(r'genres', views.GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('new_movies', views.movies, name='movies'),
    path('genre/<int:genre_id>', views.movies_by_genre, name='movies_by_genre'),
    path('video/<int:movie_id>', views.movie_video, name='movie_video'),
    path('<int:movie_id>/genres/', views.get_movie_genres, name='movie-genres'),
]

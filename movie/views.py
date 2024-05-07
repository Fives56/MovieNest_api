from django.http import Http404, JsonResponse
from movie import serializers
from rest_framework import viewsets
from .models import Genre, Movie, Video
import requests
import random
from rest_framework.pagination import PageNumberPagination

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


api_key = '1eb349bc0d7434e926252b3554fde091'

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = self.queryset
        genre = self.request.query_params.get('genre', None)
        if genre is not None:
            queryset = queryset.filter(genres__name=genre)
        return queryset

def movies(request):
    page = random.randint(1, 10)
    urlMovie = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&page={page}'
    responseMovie = requests.get(urlMovie)
    data = responseMovie.json()
    movies = data['results'][:40]

    for movie in movies:

        urlVideo = f'https://api.themoviedb.org/3/movie/{movie['id']}/videos?api_key={api_key}&language=en-US'
        responseVideo = requests.get(urlVideo)
        videos = responseVideo.json()

        if videos['results']:
            video = videos['results'][0]
            if not Video.objects.filter(id=video['id']).exists():
                new_video = Video(id=video['id'], key=video['key'], site=video['site'])
                new_video.save()

        if not Movie.objects.filter(tmdb_id=movie['id']).exists():
            new_movie = Movie(
                tmdb_id=movie['id'], 
                title=movie['title'], 
                original_title=movie['original_title'],
                adult=movie['adult'],
                backdrop_path=movie['backdrop_path'],
                original_language=movie['original_language'],
                overview=movie['overview'],
                popularity=movie['popularity'],
                poster_path=movie['poster_path'],
                release_date=movie['release_date'],
                video_id=video['id'],
                vote_average=movie['vote_average'],
                vote_count=movie['vote_count']
            )
            new_movie.save()

            for genre_id in movie['genre_ids']:
                genre, created = Genre.objects.get_or_create(id=genre_id)
                new_movie.genres.add(genre)

    return JsonResponse(movies, safe=False)

def movies_by_genre(request, genre_id):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}&sort_by=popularity.desc&page=1'
    response = requests.get(url)
    data = response.json()
    movies = data['results'][:10]  
    return JsonResponse(movies, safe=False)

def movie_video(request, movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}&language=en-US'
    response = requests.get(url)
    data = response.json()
    if data['results']:
        video = data['results'][0]
        return JsonResponse(video)
    else:
        return JsonResponse({'message': 'No se encontró video para esta película'}, status=404)
    
def get_movie_genres(request, movie_id):
    try:
        movie = Movie.objects.get(tmdb_id=movie_id)
    except Movie.DoesNotExist:
        raise Http404("La película no existe")
    genres = movie.genres.all()
    genre_names = [genre.name for genre in genres]
    return JsonResponse({'genres': genre_names}, safe=False)

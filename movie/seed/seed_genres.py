import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MovieNest_api.settings')
django.setup()

from movie.models import Genre  # Asegúrate de que esta ruta sea correcta

def seed_genres():
    api_key = '1eb349bc0d7434e926252b3554fde091'
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US'
    response = requests.get(url)
    data = response.json()
    genres = data['genres']

    for genre in genres:
        Genre.objects.get_or_create(id=genre['id'], name=genre['name'])

if __name__ == '__main__':
    seed_genres()

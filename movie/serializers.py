from rest_framework import serializers
from .models import Genre, Movie, Video

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    video = VideoSerializer(read_only=True)
    genres = GenreSerializer(read_only=True, many=True)
    class Meta:
        model = Movie
        fields = '__all__'

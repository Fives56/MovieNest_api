from django.db import models

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    original_title = models.CharField(max_length=200)
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=500, null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    original_language = models.CharField(max_length=10)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=500, null=True, blank=True)
    release_date = models.DateField()
    video = models.ForeignKey('Video', on_delete=models.CASCADE, null=True, blank=True)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

    def __str__(self):
        return self.title

class Video(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    key = models.CharField(max_length=255)
    site = models.CharField(max_length=255)

    def __str__(self):
        return self.id


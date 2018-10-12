from django.db import models


class Movie(models.Model):
    movie_link = models.CharField(max_length=100)
    movie_name = models.CharField(max_length=150)
    narrative_location = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_name

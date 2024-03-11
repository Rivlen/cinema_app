from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    description = models.TextField()
    premiere_date = models.DateField()
    duration = models.IntegerField()
    actor = models.ManyToManyField(Actor)
    director = models.CharField(max_length=100)
    production_date = models.DateField()

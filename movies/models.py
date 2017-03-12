from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date_of_birth')

class Acted_In(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE)
    salary = models.IntegerField
from django.db import models
# from smart_selects.db_fields import ChainedForeignKey 

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField('date_of_birth')
    movies = models.ManyToManyField(Movie)       

class Acted_In(models.Model):
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE)
        # chained_field="movie",
        # chained_model_field="movie",
        # show_all=False,
        # auto_choose=True,
        # sort=True 
   
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
        # chained_field="actor",
        # chained_model_field="actor",
        # show_all=False,
        # auto_choose=True,
        # sort=True 
    
    salary = models.IntegerField(default=0)
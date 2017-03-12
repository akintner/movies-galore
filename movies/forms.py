from django import forms
from movies.models import Movie 
from movies.models import Actor

class MovieForm(forms.Form):
  movie_title = forms.CharField(max_length=200, required=True)
  movie_genre = forms.CharField(max_length=200, required=True)

class ActorForm(forms.Form):
  actor_name = forms.CharField(max_length=200, required=True)
  actor_date_of_birth = forms.DateField(required=True)

class ActedInForm(forms.Form):
  movie_id = forms.ModelChoiceField(queryset=Movie.objects.all().order_by('title'))
  actor_id = forms.ModelChoiceField(queryset=Actor.objects.all().order_by('name'))
  salary = forms.IntegerField(required=True)
from django import forms

class MovieForm(forms.Form):
  movie_title = forms.CharField(max_length=200, required=True)
  movie_genre = forms.CharField(max_length=200, required=True)

class ActorForm(forms.Form):
  actor_name = forms.CharField(max_length=200, required=True)
  actor_date_of_birth = forms.DateField(required=True)



from django.shortcuts import render
from django.http import HttpResponse

from movies.models import Movie 
from movies.models import Actor
from movies.models import Acted_In

from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/movies.html', context)

def moviesLoad(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('index'))
    else:
        form = MovieForm()

    return render(request, 'movies/load/movieform.html', {
        'form': form,
    })



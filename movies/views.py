from django.shortcuts import render
from django.http import HttpResponse

from movies.models import Movie 
from movies.models import Actor
from movies.models import Acted_In

from .forms import MovieForm
from .forms import ActorForm
from .forms import ActedInForm

def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/movies.html', context)

def actors(request):
    actors = Actor.objects.all()
    context = {'actors': actors}
    return render(request, 'movies/actors.html', context)

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

def moviesLoadActor(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('movies/actors-index'))
    else:
        form = ActorForm()

    return render(request, 'movies/load/actorform.html', {
        'form': form,
    })

def moviesLoadJoin(request):
    if request.method == 'POST':
        form = ActedInForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ActedInForm()

    return render(request, 'movies/load/actedinform.html', {
        'form': form,
    })



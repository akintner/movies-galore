from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum

from movies.models import Movie 
from movies.models import Actor
from movies.models import Acted_In

from .forms import MovieForm
from .forms import ActorForm
from .forms import ActedInForm
# from .forms import SeedDataForm
from .forms import ActorsMoviesForm

def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/movies.html', context)

def actors(request):
    actors = Actor.objects.all()
    context = {'actors': actors}
    return render(request, 'movies/actors.html', context)

def seed(request):
    if request.method == 'POST':
        form = SeedDataForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SeedDataForm()

    return render(request, 'movies/load/seedform.html', {
        'form': form,
    })

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

def choice(request):
    if request.method == 'POST':
        form = ActorsMoviesForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('actor-table'))
    else:
        form = ActorsMoviesForm()
    return render(request, 'movies/choice.html', { 'form': form, })
        
def table(request, search_id):
    salary_average = Acted_In.objects.filter(actor_id=search_id).aggregate(Sum('salary'))
    movies = Acted_In.objects.filter(actor_id=search_id)
    return render(request, 'movies/table.html')


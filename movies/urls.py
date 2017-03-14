from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^actors/', views.actors, name='actors-index'),
    url(r'^load/', views.moviesLoad, name='load'),
    url(r'^loadactor/', views.moviesLoadActor, name='actor-load'),
    url(r'^loadjoin/', views.moviesLoadJoin, name='acted-in-load'),
    url(r'^seed', views.seed, name='seed'),
    url(r'^actortable/', views.table, name='actor-choice'),
    # url(r'^actorchoice/(?P<search_id>\d+)', views.table, name='actor-table'),
]
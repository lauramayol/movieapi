
from django.urls import path
from . import views

urlpatterns = [
    path('load', views.movie_load, name='movie_load'),
    path('', views.movie_locations, name='movie_locations'),
]

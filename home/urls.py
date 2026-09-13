# this file contains path relating to url of home app

from django.urls import path #defines URL patterns in django

from . import views #template
urlpatterns = [
    path('', views.index, name='home.index'), #add path for home app
    path('about', views.about, name='home.about'),
]
from django.urls import path
from . import views

app_name = 'home'   # namespace

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('generos/', views.genero, name='genero'),
]

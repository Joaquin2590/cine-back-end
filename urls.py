from django.urls import path
from . import views

app_name = 'home'   # namespace

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('genero/<slug:slug>/', views.genero, name='genero'),
]

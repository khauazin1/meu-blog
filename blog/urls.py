from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('cursos/', views.cursos, name='cursos'),
    path('interesses/', views.interesses, name='interesses'),
]
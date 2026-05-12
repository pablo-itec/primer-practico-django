from django.urls import path
from . import views

urlpatterns = [
    path('', views.registros, name='registros'),
    path('cargar-mascota/', views.cargar_mascota, name='cargar_mascota'),
                ]


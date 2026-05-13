from django.urls import path
from . import views

urlpatterns = [
    path('', views.registros, name='registros'),
    path('cargar-mascota/', views.cargar_mascota, name='cargar_mascota'),
    path('registros/', views.registros, name='registros'),
    path('editar/<int:id_mascota>/', views.editar_mascota, name='editar_mascota'),
    path('eliminar/<int:id_mascota>/', views.eliminar_mascota, name='eliminar_mascota'),
                ]


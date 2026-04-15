from django.urls import path
from . import views

urlpatterns = [
    path('', views.bienvenido, name='bienvenido'),
    path('about/', views.sobreNosotros, name='sobreNosotros'),
        ]


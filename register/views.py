from django.shortcuts import render
from django.http import HttpResponse
from .models import Registro

def registros(request):
    registros_db = Registro.objects.all() 
    return render(request, "appvete/register.html", {"registros": registros_db})
    
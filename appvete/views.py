from django.shortcuts import render
from django.http import HttpResponse

ulises = "crack"
def bienvenido(request):
    return render(request, "appvete/index.html",)

def sobreNosotros(request):
    return render(request, "appvete/about.html",)


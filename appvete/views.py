from django.shortcuts import render

ulises = "crack"
def bienvenido(request):
    return render(request, "appvete/index.html",)


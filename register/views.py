from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registro
from .forms import MascotaForm

def registros(request):
    registros_db = Registro.objects.all() 
    return render(request, "appvete/register.html", {"registros": registros_db})
    



def cargar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('admin:index')
    else:
        form = MascotaForm()
    
    return render(request, 'register/formulario_mascota.html', {'form': form})
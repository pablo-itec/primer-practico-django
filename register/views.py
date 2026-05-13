from django.shortcuts import render, redirect, get_object_or_404
from .models import Registro
from .forms import MascotaForm

def registros(request):
    registros_db = Registro.objects.all() 
    return render(request, "register/registros.html", {"registros": registros_db})

def cargar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('registros')
    else:
        form = MascotaForm()
    
    return render(request, 'register/formulario_mascota.html', {'form': form})

def editar_mascota(request, id_mascota):
    mascota = get_object_or_404(Registro, id=id_mascota)
    
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        
        if form.is_valid():
            form.save()
            return redirect('registros') 
    else:
        form = MascotaForm(instance=mascota)
    
    return render(request, 'register/formulario_mascota.html', {'form': form, 'editando': True})

def eliminar_mascota(request, id_mascota):
    mascota = get_object_or_404(Registro, id=id_mascota)
    
    if request.method == 'POST':
        mascota.delete() 
        return redirect('registros') 
        
    return render(request, 'register/confirmar_eliminar.html', {'mascota': mascota})
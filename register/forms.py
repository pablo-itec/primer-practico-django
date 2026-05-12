from django import forms
from .models import Registro

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Registro
        # Incluimos los campos que el usuario debe llenar
        fields = ['nombre', 'especie', 'raza', 'edad', 'duenio']
        
        # Opcional: añadimos clases de CSS para que se vea bien (estilo Bootstrap)
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especie': forms.TextInput(attrs={'class': 'form-control'}),
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'duenio': forms.Select(attrs={'class': 'form-control'}),
        }
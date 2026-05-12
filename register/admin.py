from django.contrib import admin
# Importamos usando la ruta completa para evitar errores de punto relativo
from register.models import Duenio, Registro

@admin.register(Duenio)
class DuenioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni')
    search_fields = ('nombre', 'dni')
    list_filter = ('apellido',)

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie',)
    search_fields = ('nombre', 'especie')
    list_filter = ('especie',)
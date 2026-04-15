from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=2)
    dueños = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Soy {self.nombre} un {self.especie} raza {self.raza}, tengo {self.edad} y mis dueños son {self.dueños}"

    
    
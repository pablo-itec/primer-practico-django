from django.db import models

# Create your models here.

class Duenio(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    



class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField() 
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    duenio = models.ForeignKey(Duenio, on_delete=models.CASCADE, null=True, related_name="mascotas")

    
    def __str__(self):
        return f"Soy {self.nombre} un {self.especie} raza {self.raza}, tengo {self.edad} anios y mi dueño es {self.duenio}"
    
    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animales"

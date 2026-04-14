from django.db import models

class animal(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    especie = models.CharField(max_length=50)

    def __str__(self):
        return f'tu mascota se llama {self.nombre}'
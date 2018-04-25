from django.db import models

# Create your models here.

class Mascota(models.Model):
	nombre = models.Charfield(max_length=50)
	sexo = models.Charfield(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	
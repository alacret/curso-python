from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length = 120, blank=False)

class Articulo(models.Model):
	titulo = models.CharField(max_length = 120, blank=False)
	autor = models.ForeignKey(Persona)

class comentario(models.Model):
	comentario = models.CharField(max_length = 120, blank=False)
	articulo = models.ForeignKey(Articulo)
	autor = models.ForeignKey(Persona)

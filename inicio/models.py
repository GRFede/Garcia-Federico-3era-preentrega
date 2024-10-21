from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    fecha_nacimiento=models.DateField()

class Personales(models.Model):
    nombres =models.CharField(max_length=20)
    apellidos =models.CharField(max_length=20)
    edad =models.IntegerField()
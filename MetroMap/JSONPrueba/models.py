from django.db import models

# Create your models here.

class Estacion(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    estado = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
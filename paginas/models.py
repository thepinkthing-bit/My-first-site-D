from django.db import models

class Movie(models.Model):
    Título = models.CharField(max_length=100)
    Ano = models.IntegerField()
    Genêro = models.CharField(max_length=50)
    Nota = models.FloatField(max_length=100)
    Estúdio = models.CharField(max_length=100)


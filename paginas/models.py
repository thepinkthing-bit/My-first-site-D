from django.db import models

class Category(models.Model):
    Name = models.CharField(max_length=100, unique=True)
    def __str__(self):
       return self.Name
    
class Movie(models.Model):
    Título = models.CharField(max_length=100)
    Ano = models.IntegerField()
    Genêro = models.CharField(max_length=50)
    Nota = models.FloatField(max_length=100)
    Estúdio = models.CharField(max_length=100)
    Categoria = models.ForeignKey(
        Category,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
    )
from django import forms
from .models import Movie, Category

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['Título', 'Ano', 'Nota', 'Estúdio', 'Genêro', 'Categoria']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['Name']
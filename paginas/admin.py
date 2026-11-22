from django.contrib import admin

from .models import Movie, Category

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["Título", "Ano", "Genêro", "Nota", "Estúdio", "Categoria"]

admin.site.register(Category)
admin.site.register(Movie, ProjectAdmin)

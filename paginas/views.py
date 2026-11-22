from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Movie, Category
from collections import defaultdict
from paginas.forms import MovieForm, CategoryForm

def Start (request):
    dados = {
        "name": "The Pink Thing",
        "age": "20 years",
        "height": "1.67",
        "Information": ["Mr. WPNZ", "Mr. Puzzles"],
        "Hobbies": ["Heading books", "spending time with my best dad <3"],
        "City": ["The Big Bad's Lair"],
    }
    return render(request, "start.html", dados)


def About (request):
    return render(request, "about.html")

def Contact (request):
    return render(request, "contact.html")

def Movies (request):
    projects = {
            "projects": Movie.objects.all(),
    }
    return render(request, "projects.html", projects)

def Categories (request):
    Context = {
                "Categories": Movie.objects.select_related("Categoria").order_by("Categoria", "Título")
        }
    return render(request, "Categories.html", Context)

def New_Movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/New Movie/")
    else:
        form = MovieForm()
    return render(request, "New_Movie.html",
                  {"form": form})

def New_Categories(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/New Categories/")
    else:
        form = MovieForm()
    return render(request, "New_Categories.html",
                  {"form": form})
                                  
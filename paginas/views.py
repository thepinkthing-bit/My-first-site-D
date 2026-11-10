from django.shortcuts import render

from django.http import HttpResponse

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
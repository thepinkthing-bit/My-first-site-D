from django.shortcuts import render

from django.http import HttpResponse

def início (request):
    dados = {
        "name": "The Pink Thing",
        "age": "20 years",
        "height": "1.67",
        "Information": ["Mr. WPNZ", "Mr. Puzzles"]
    }
    return render(request, "inicio.html", dados)


def sobre (request):
    return HttpResponse("<h1>About me</h1>"
                        "<p>My name is The Pink Thing!! :D </p>"
                        "<a href='/'>Initiation</a> | "
                        "<a href='/About/'>About</a> | "
                        "<a href='/Contact/'>Contact</a>")

def contato (request):
    return HttpResponse("<h1>Contact</h1>"
                        "You can find me on my e-mail: barbosasamara680@gmail.com</p>"
                        "My phone number is: (81) 9 8415-1287</p>"
                        "My Instagram: @misuki_.sam_</p>"
                        "<a href='/'>initiation</a> | "
                        "<a href='/About/'>About</a> | "
                        "<a href='/Contact/'>Contact</a>")
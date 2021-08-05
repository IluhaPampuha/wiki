from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def wiki(request):
    return render(request, 'wiki_app/home.html')


def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
    if request.GET.get("special"):
        characters.extend("!@#$%^&*()_+")
    length = int(request.GET.get("length", 12))
    if length > 14: length = 14
    elif length < 6: length = 6
    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'wiki_app/password.html', {"password": thepassword})

def about(request):
    return render(request, 'wiki_app/about.html')
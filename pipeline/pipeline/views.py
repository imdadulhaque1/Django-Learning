#This is created by me----------------->>Imdadul Haque
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    addingName = {'name': 'Imdadul Haque', 'place': 'Tarash, Sirajgonj'}
    return render(request, 'index.html',addingName)
    #return HttpResponse("Home Page")

def removepunc(request):
    return  HttpResponse("Remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("New Line remove")

def spaceremove(request):
    return  HttpResponse("Space Remove <a href='/'>Back</a>")

def charcount(request):
    return HttpResponse("Character count")
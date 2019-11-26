#This is created b y me------------>>>Imdadul Haque
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    addname= {'name':'Imdadul Haque', 'Birthdayplace': 'Sobuj-para, Tarash, Sirajgonj'}
    return render(request,'index.html',addname)
    #return HttpResponse("Home Page")
def about(request):
    return HttpResponse("Here is included about myself which is visible to another. <a href='/'>Back to Home</a>")
def spaceRemove(request):
    return HttpResponse("Remove the unnecessary Space. <a href='/'>Back to Home</a>")
def nlineremove(request):
    return HttpResponse("Remove the extra newline in a page. <a href='/'>Back to Home</a>")
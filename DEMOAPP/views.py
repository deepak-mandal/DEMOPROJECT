from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hi(request):
    return render(request, "DEMOAPP/index.html")
    #return HttpResponse("<h1> This is my Home Page</h1>")

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 

def index(request):
    name = "world"
    return render(request,"base.html", {"name":name})
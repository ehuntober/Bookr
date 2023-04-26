from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greeting_view(request):
    """Greet the user"""
    return HttpResponse("Hey there, welcome to Bookr!, Your one stop place to review books")
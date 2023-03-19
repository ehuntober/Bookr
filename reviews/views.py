from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 

def index(request):
    name = request.Get.get("name") or "world"
    return HttpResponse("Hello, {}".format(name))
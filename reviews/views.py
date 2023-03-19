from django.shortcuts import render

from django.http import HttpResponse 
from django.views.generic import TemplateView

class HomePage(TemplateView):
    TemplateVeiw ='home_page.html'



def index(request):
    name = "world"
    return render(request,"base.html", {"name":name})
from django.contrib import admin 
from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.welcome_view,name='index'),
    path('books/', views.book_list , name='book_list')
]

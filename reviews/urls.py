from django.urls import path
from . import views
from reviews.admin import admin_site

urlpatterns = [
    path('admin/',admin_site.urls),
    path('', views.index),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('book-search/', views.book_search, name='book_search'),
    path('',include('reviews.urls'))
]
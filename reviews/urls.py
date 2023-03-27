from reviews.admin import admin_site

from django.urls import path , include
from . import views

# new url
urlpatterns = [
    path('admin/', admin_site.urls),
    path('', views.index),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('book-search/', views.book_search, name='book_search'),
    
    # path('',include('reviews.urls'))
    path('publishers/<int:pk>/', views.publisher_edit,name="publisher_edit"),
    path('publishers/new/', views.publisher_edit,name='publisher_create')
]

#   path('admin/',admin_site.urls),
#NameError: name 'admin_site' is not defined

from reviews.admin import admin_site

from django.urls import path , include
from . import views , api_views


from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', api_views.BookViewSet)
router.register(r'reviews', api_views.ReviewViewSet)


# new url
urlpatterns = [
    path('admin/', admin_site.urls),
 path('', views.index),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/<int:book_pk>/reviews/new/', views.review_edit, name='review_create'),
    path('books/<int:book_pk>/reviews/<int:review_pk>/', views.review_edit, name='review_edit'),
    path('books/<int:pk>/media/', views.book_media, name='book_media'),
    path('book-search/', views.book_search, name='book_search'),
    path('publishers/<int:pk>/',views.publisher_edit, name='publisher_edit'),
    path('publishers/new/',views.publisher_edit, name='publisher_create'),
    
    # api urls
    path('api/first_api_view/', api_views.first_api_view),
    # path('api/all_books/', api_views.all_books, name='all_books'),
    path('api/all_books/', api_views.AllBooks.as_view(),name='all_books'),
    path('api/contributors/', api_views.ContributorView.as_view(), name='contributors'),
    
    path('api/login', api_views.Login.as_view(), name='login'),
    path('api/', include((router.urls, 'api'))),
    
    
]

#   path('admin/',admin_site.urls),
#NameError: name 'admin_site' is not defined

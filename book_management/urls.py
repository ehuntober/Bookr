from django.urls import path

from .views import BookRecordFormView, FormSuccessView , BookUpdateView ,BookDeleteView

urlpatterns = [
    path('new_book_record', BookRecordFormView.as_view(), name='book_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
    path('book_record_update/<int:pk>',BookUpdateView.as_view(),name="book_update"),
    path('book_record_delete/<int:pk>', BookDeleteView.as_view(), name="book_delete")
]
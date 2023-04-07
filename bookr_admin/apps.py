# from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


# class BookrAdminConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'bookr_admin'
    
class BookrAdminConfig(AdminConfig):
    default_site = 'bookr_admin.admin.BookrAdmin'

# from django.contrib import admin
# from django.contrib.auth.admin import User

# class BookrAdmin(admin.AdminSite):
#     site_header = "Bookr Administration"

# admin_site = BookrAdmin(name='bookr_admin')
# admin_site.register(User)

from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Administration"
    logout_template = "admin/logout.html"


def profile_view(self,request):
    
from django.contrib.admin import AdminSite
from django.contrib import admin


from reviews.models import (Publisher, Contributor , Book , \
    BookContributor, Review )

class BookrAdminSite(AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'
    
admin_site = BookrAdminSite(name='bookr')


admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)

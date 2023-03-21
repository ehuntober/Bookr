from django.contrib.admin import AdminSite
from django.contrib import admin


from reviews.models import (Publisher, Contributor , Book , \
    BookContributor, Review )

class BookrAdminSite(AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'
    
admin_site = BookrAdminSite(name='bookr')

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title','isnb')
    list_filter = ['publisher','publication_date']
    search_fields = ('title', 'isnb','publisher__name')
    
class  ReviewAdmin(admin.ModelAdmin):
    exclude=['date_edited']
    fieldsets = (
        (None, {
            "fields": (
                'creator', 'book'
            ),
            
            (
                'Review content',{
                    "fields":('content','rating')
                }
            )
        }),
    )
    


admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)

from django.contrib.admin import AdminSite
from django.contrib import admin


from reviews.models import (Publisher, Contributor , Book , \
    BookContributor, Review )

class BookrAdminSite(AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'
    
admin_site = BookrAdminSite(name='bookr')



def initialled_name(obj):
    """ obj.first_names='Jerome David', obj.last_names='Salinger'
        => 'Salinger, JD' """
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')

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
            )}),
            
            (
                'Review content',{
                    "fields":('content','rating')
                }
            )
    )
    


admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)

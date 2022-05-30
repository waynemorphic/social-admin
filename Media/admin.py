from django.contrib import admin
from Media.models import User, Category, Location, Image

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    '''
    class allows ordering of many to many fields
    '''
    # filter_horizontal = ('image_category', 'image_location')
    
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image, ImageAdmin)
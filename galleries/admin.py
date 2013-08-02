from django.contrib import admin
from galleries.models import Image, Gallery
from sorl.thumbnail.admin import AdminImageMixin

class ImageInlineAdmin(admin.TabularInline, AdminImageMixin):
    model = Image

class ImageAdmin(admin.ModelAdmin, AdminImageMixin):
    list_display = ('title','price', 'description')
    search_fields = ('title','price')
    
class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        ImageInlineAdmin
    ]

admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)

from django.contrib import admin
from galleries.models import Image, Gallery
from sorl.thumbnail.admin import AdminImageMixin

class ImageAdmin(admin.ModelAdmin, AdminImageMixin):
    list_display = ('title','price', 'description')
    search_fields = ('title','price')

class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)

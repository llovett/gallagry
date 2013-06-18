from django.contrib import admin
from frontpage.models import GalleryLinkPosition, BlogLinkPosition

class GLPositionAdmin(admin.ModelAdmin):
    pass

class BLPositionAdmin(admin.ModelAdmin):
    pass

admin.site.register(GalleryLinkPosition, GLPositionAdmin)
admin.site.register(BlogLinkPosition, BLPositionAdmin)

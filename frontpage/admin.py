from django.contrib import admin
from frontpage.models import GalleryLinkPosition, BlogLinkPosition

class FrontPageAdmin(admin.ModelAdmin):
    verbose_name = "Front Page"

class GLPositionAdmin(FrontPageAdmin):
    pass

class BLPositionAdmin(FrontPageAdmin):
    pass

admin.site.register(GalleryLinkPosition, GLPositionAdmin)
admin.site.register(BlogLinkPosition, BLPositionAdmin)

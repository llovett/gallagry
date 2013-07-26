from django.contrib import admin
from frontpage.models import GalleryLinkPosition, BlogLinkPosition, Tagline

class FrontPageAdmin(admin.ModelAdmin):
    verbose_name = "Front Page"

class GLPositionAdmin(FrontPageAdmin):
    pass

class BLPositionAdmin(FrontPageAdmin):
    pass

class TaglineAdmin(FrontPageAdmin):
    pass

admin.site.register(GalleryLinkPosition, GLPositionAdmin)
admin.site.register(BlogLinkPosition, BLPositionAdmin)
admin.site.register(Tagline, TaglineAdmin)

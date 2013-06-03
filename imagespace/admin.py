from django.contrib import admin
from imagespace.models import ImageFrame

class ImageFrameAdmin(admin.ModelAdmin):
    pass

admin.site.register(ImageFrame, ImageFrameAdmin)

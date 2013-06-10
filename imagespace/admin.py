from django.contrib import admin
from imagespace.models import ImageFrame
from sorl.thumbnail.admin import AdminImageMixin

class ImageFrameAdmin(admin.ModelAdmin, AdminImageMixin):
    exclude = ('geometry',)

admin.site.register(ImageFrame, ImageFrameAdmin)

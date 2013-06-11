from django.contrib import admin
from imagespace.models import ImageFrame
from imagespace.forms import ImageFrameForm
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail.admin import AdminImageMixin

class ImageFrameAdmin(admin.ModelAdmin, AdminImageMixin):
    form = ImageFrameForm
    fieldsets = (
        (None, {'fields':('image','title','price','description','visible')}),
        (_('Advanced options'), {'classes':('collapse',), 'fields': ('width',
                                                                     'height',
                                                                     'manual_positioning',
                                                                     'pos_x',
                                                                     'pos_y')})
    )
    list_display = ('title','price')
    search_fields = ('title','price')

admin.site.register(ImageFrame, ImageFrameAdmin)

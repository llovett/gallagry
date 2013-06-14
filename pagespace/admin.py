from django.contrib import admin
from pagespace.models import FlatPage, GalleryLinkPosition
from django.utils.translation import ugettext_lazy as _
from pagespace.forms import FlatpageForm

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Link Options'), {'classes': ('grp-collapse grp-open',),
                             'fields': ('pos_x',
                                        'pos_y',
                                        'rotation')}),
    )
    list_display = ('url', 'title')
    search_fields = ('url', 'title')

class GLPositionAdmin(admin.ModelAdmin):
    pass

admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(GalleryLinkPosition, GLPositionAdmin)

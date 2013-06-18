from django.contrib import admin
from pagespace.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from pagespace.forms import FlatpageForm
from mce_filebrowser.admin import MCEFilebrowserAdmin

class FlatPageAdmin(MCEFilebrowserAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'background_image', 'colorscheme',)}),
        (_('Link Options'), {'classes': ('grp-collapse grp-open',),
                             'fields': ('pos_x',
                                        'pos_y',
                                        'rotation')}),
    )
    list_display = ('url', 'title')
    search_fields = ('url', 'title')

admin.site.register(FlatPage, FlatPageAdmin)

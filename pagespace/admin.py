from django.contrib import admin
from pagespace.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from pagespace.forms import FlatpageForm

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content')}),
        (_('Advanced options'), {'classes': ('grp-collapse grp-closed',),
                                 'fields': ('manual_positioning',
                                            'pos_x',
                                            'pos_y')}),
    )
    list_display = ('url', 'title')
    search_fields = ('url', 'title')

admin.site.register(FlatPage, FlatPageAdmin)

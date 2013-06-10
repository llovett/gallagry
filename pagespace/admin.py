from django.contrib import admin
from pagespace.models import FlatPage
from django.utils.translation import ugettext_lazy as _
from pagespace.forms import FlatpageForm

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments',
                                                                      'registration_required',
                                                                      'template_name',
                                                                      'manual_positioning',
                                                                      'pos_x',
                                                                      'pos_y')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')

admin.site.register(FlatPage, FlatPageAdmin)

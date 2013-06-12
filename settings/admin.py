from django.contrib import admin
from settings.models import ColorScheme

class ColorSchemeAdmin(admin.ModelAdmin):
    pass

admin.site.register(ColorScheme, ColorSchemeAdmin)

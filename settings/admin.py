from django.contrib import admin
from settings.models import ColorScheme, BackgroundImage

class ColorSchemeAdmin(admin.ModelAdmin):
    pass

class BackgroundImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(ColorScheme, ColorSchemeAdmin)
admin.site.register(BackgroundImage, BackgroundImageAdmin)

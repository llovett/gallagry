from django.contrib import admin
from settings.models import ColorScheme, BackgroundImage

class SettingsAdmin(admin.ModelAdmin):
    verbose_name = "Look and Feel"

class ColorSchemeAdmin(SettingsAdmin):
    pass

class BackgroundImageAdmin(SettingsAdmin):
    pass

admin.site.register(ColorScheme, ColorSchemeAdmin)
admin.site.register(BackgroundImage, BackgroundImageAdmin)

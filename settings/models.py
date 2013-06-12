from django.db import models
from colorful.fields import RGBColorField
from django.utils.translation import ugettext_lazy as _
import datetime

class ColorScheme(models.Model):
    background_color = RGBColorField(verbose_name="Background color")
    foreground_color = RGBColorField(verbose_name="Foreground color")
    link_color = RGBColorField(verbose_name="Normal link color")
    rollover_color = RGBColorField(verbose_name="Rollover link color")
    is_default = models.BooleanField(default=True, verbose_name="Make this your default color scheme")
    last_updated = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return "Color scheme from %s"%self.last_updated.strftime("%d/%m/%Y at %I:%M %p")

    def save(self):
        if self.is_default:
            other_schemes = ColorScheme.objects.exclude(id=self.id)
            for scheme in other_schemes:
                scheme.is_default = False
                scheme.save()
        super(ColorScheme,self).save()

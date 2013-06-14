from django.db import models
from colorful.fields import RGBColorField
from django.utils.translation import ugettext_lazy as _
import datetime

class ColorScheme(models.Model):
    title = models.CharField(max_length=200, default="Color scheme from %s"%datetime.datetime.now().strftime("%d/%m/%Y at %I:%M %p"))
    background_color = RGBColorField(verbose_name="Background color")
    foreground_color = RGBColorField(verbose_name="Foreground color")
    link_color = RGBColorField(verbose_name="Normal link color")
    rollover_color = RGBColorField(verbose_name="Rollover link color")
    is_default = models.BooleanField(default=True, verbose_name="Make this your default color scheme")

    def __unicode__(self):
        return self.title

    def save(self):
        if self.is_default:
            other_schemes = ColorScheme.objects.exclude(id=self.id)
            for scheme in other_schemes:
                scheme.is_default = False
                scheme.save()
        super(ColorScheme,self).save()

class BackgroundImage(models.Model):
    background_image = models.ImageField(upload_to='images')
    is_default = models.BooleanField(default=True, verbose_name="Make this your default background")

    def __unicode__(self):
        return self.background_image.name

    def save(self):
        if self.is_default:
            other_imgs = BackgroundImage.objects.exclude(id=self.id)
            for img in other_imgs:
                img.is_default = False
                img.save()
        super(BackgroundImage,self).save()

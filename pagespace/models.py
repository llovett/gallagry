from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

class FlatPage(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    background_image = models.ForeignKey('settings.BackgroundImage', verbose_name="Background image", blank=True, null=True)
    colorscheme = models.ForeignKey('settings.ColorScheme', verbose_name="Color scheme", blank=True, null=True)

    # Link options
    pos_x = models.IntegerField(default=0, verbose_name="X Position")
    pos_y = models.IntegerField(default=0, verbose_name="Y Position")
    rotation = models.DecimalField(max_digits=8,decimal_places=5, default=0, verbose_name="Rotation")

    class Meta:
        verbose_name = _('custom page')
        ordering = ('url',)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url

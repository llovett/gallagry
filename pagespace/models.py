from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

class FlatPage(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)

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

class GalleryLinkPosition(models.Model):
    pos_x = models.IntegerField(default=0, verbose_name="X Position")
    pos_y = models.IntegerField(default=0, verbose_name="Y Position")
    rotation = models.DecimalField(max_digits=8,decimal_places=5, default=0, verbose_name="Rotation")
    is_default = models.BooleanField(default=True, verbose_name="Make this the default gallery link position")

    def __unicode__(self):
        return "gallery at (%d,%d) rotated %f"%(self.pos_x,self.pos_y,self.rotation)

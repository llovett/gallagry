from django.db import models
from django.utils.translation import ugettext_lazy as _
from tagging.fields import TagField

class Entry(models.Model):
    title = models.CharField(_("Title"), max_length=500)
    content = models.TextField(_("Content"))
    slug = models.SlugField(max_length=500)
    tags = TagField(_("Tags"), max_length=1000, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

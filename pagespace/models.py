from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class FlatPage(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    enable_comments = models.BooleanField(_('enable comments'))
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
        help_text=_("Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
    registration_required = models.BooleanField(_('registration required'), help_text=_("If this is checked, only logged-in users will be able to view the page."))
    sites = models.ManyToManyField(Site)

    manual_positioning = models.BooleanField(default=False, verbose_name="Position this manually",
                                             help_text=_("Enabling this will allow you to pick an exact position for the link to this page on the main page. Otherwise, the link will flow naturally."))
    pos_x = models.IntegerField(default=0, verbose_name="X Position")
    pos_y = models.IntegerField(default=0, verbose_name="Y Position")

    class Meta:
        verbose_name = _('stylized flat page')
        verbose_name_plural = _('stylized flat pages')
        ordering = ('url',)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url
from django import forms
from django.conf import settings
from pagespace.models import FlatPage
from django.utils.translation import ugettext, ugettext_lazy as _
from tinymce.widgets import TinyMCE

class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/\.~]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " dots, underscores, dashes, slashes or tildes."))

    # Override ugly textfield widget with tinymce
    content = forms.CharField(widget=TinyMCE(attrs={'cols':80,'rows':50}))

    class Meta:
        model = FlatPage

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url.startswith('/'):
            raise forms.ValidationError(ugettext("URL is missing a leading slash."))
        if (settings.APPEND_SLASH and
            'django.middleware.common.CommonMiddleware' in settings.MIDDLEWARE_CLASSES and
            not url.endswith('/')):
            raise forms.ValidationError(ugettext("URL is missing a trailing slash."))
        return url

    def clean(self):
        url = self.cleaned_data.get('url', None)

        same_url = FlatPage.objects.filter(url=url)
        if self.instance.pk:
            same_url = same_url.exclude(pk=self.instance.pk)

        return super(FlatpageForm, self).clean()

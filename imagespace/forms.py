from django import forms
from imagespace.models import ImageFrame
from django.utils.translation import ugettext, ugettext_lazy as _

class ImageFrameForm(forms.ModelForm):
    class Meta:
        model = ImageFrame

# -*- coding: utf-8 -*-
from django.conf import settings
from django.forms.widgets import TextInput
from django.utils.safestring import SafeUnicode

try:
    url = settings.STATIC_URL
except AttributeError:
    try:
        url = settings.MEDIA_URL
    except AttributeError:
        url = ''

class ColorFieldWidget(TextInput):
    class Media:
        css = {
            # TODO: make some CSS for this. This stylesheet is unused!
            'all': ("%scolorful/colorPicker.css" % url,)
        }
        js = ("%scolorful/jscolor.js"%url,)

    input_type = 'color'

    def render(self, name, value, attrs={}):
        if not 'id' in attrs:
            attrs['id'] = "#id_%s" % name
        attrs['class'] = 'color {hash:true,caps:false}'
        return super(ColorFieldWidget, self).render(name, value, attrs)

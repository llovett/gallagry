from django import forms
from tinymce.widgets import TinyMCE
from barebones.models import Entry

class EntryForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols':80,'rows':50}))

    class Meta:
        model = Entry

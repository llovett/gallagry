from django.contrib import admin
from barebones.forms import EntryForm
from barebones.models import Entry
from mce_filebrowser.admin import MCEFilebrowserAdmin

class EntryAdmin(MCEFilebrowserAdmin):
    form = EntryForm
    prepopulated_fields = {"slug":("title",)}
    search_fields = ('title','content')
    verbose_name = "News"

admin.site.register(Entry, EntryAdmin)

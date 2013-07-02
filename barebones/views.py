from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from barebones.models import Entry
from settings import models as prefs
from tagging.models import Tag, TaggedItem
from re import sub
from functools import wraps

def get_prefs(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        try:
            colorscheme = prefs.ColorScheme.objects.get(use_for_blog=True)
        except prefs.ColorScheme.DoesNotExist:
            colorscheme = None
        try:
            bgimage = prefs.BackgroundImage.objects.get(use_for_blog=True)
        except prefs.BackgroundImage.DoesNotExist:
            bgimage = None
        return view(request, colorscheme, bgimage, *args, **kwargs)
    return wrapper
    
@get_prefs
def main_page(request, colorscheme, bgimage):
    entries = Entry.objects.all()
    return render_to_response("barebones-all.html", locals(), context_instance=RequestContext(request))

@get_prefs
def get_tagged(request, colorscheme, bgimage, slugified_tag):
    # Have to look through all the tags, because of multi-word tag/slugify issue
    all_tags = Tag.objects.usage_for_model(Entry)
    tag = None
    for cur in all_tags:
        if sub(' ','-',cur.name) == slugified_tag:
            tag = cur
            break
    tag = Tag.objects.get(name=tag)
    entries = TaggedItem.objects.get_by_model(Entry, tag)
    return render_to_response("barebones-tag.html", locals(), context_instance=RequestContext(request))

@get_prefs
def get_post(request, colorscheme, bgimage, slugified_title):
    entry = get_object_or_404(Entry, slug=slugified_title)
    return render_to_response("barebones-entry.html", locals(), context_instance=RequestContext(request))

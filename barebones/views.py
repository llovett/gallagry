from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404
from django.template import RequestContext
from barebones.models import Entry
from settings import models as prefs
from tagging.models import Tag, TaggedItem
from re import sub

def main_page(request):
    entries = Entry.objects.all()
    try:
        colorscheme = prefs.ColorScheme.objects.get(use_for_blog=True)
    except prefs.ColorScheme.DoesNotExist:
        pass
    try:
        bgimage = prefs.BackgroundImage.objects.get(use_for_blog=True)
    except prefs.BackgroundImage.DoesNotExist:
        pass
    return render_to_response("entry_list.html", locals(), context_instance=RequestContext(request))

def get_tagged(request, slugified_tag):
    # Have to look through all the tags, because of multi-word tag/slugify issue
    all_tags = Tag.objects.usage_for_model(Entry)
    tag = None
    for cur in all_tags:
        if sub(' ','-',cur.name) == slugified_tag:
            tag = cur
            break
    tag = Tag.objects.get(name=tag)
    entries = TaggedItem.objects.get_by_model(Entry, tag)
    try:
        colorscheme = prefs.ColorScheme.objects.get(use_for_blog=True)
    except prefs.ColorScheme.DoesNotExist:
        pass
    try:
        bgimage = prefs.BackgroundImage.objects.get(use_for_blog=True)
    except prefs.BackgroundImage.DoesNotExist:
        pass
    return render_to_response("entry_list.html", locals(), context_instance=RequestContext(request))

def get_post(request, slugified_title):
    entry = get_object_or_404(Entry, slug=slugified_title)
    try:
        colorscheme = prefs.ColorScheme.objects.get(use_for_blog=True)
    except prefs.ColorScheme.DoesNotExist:
        pass
    try:
        bgimage = prefs.BackgroundImage.objects.get(use_for_blog=True)
    except prefs.BackgroundImage.DoesNotExist:
        pass
    return render_to_response("single_entry.html", locals(), context_instance=RequestContext(request))

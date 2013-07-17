from django.http import HttpResponse, HttpResponseBadRequest
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from pagespace.models import FlatPage
from galleries.models import Gallery
from frontpage.models import GalleryLinkPosition, BlogLinkPosition
from settings.models import BackgroundImage, ColorScheme
import json

def main_page(request):
    gallery_link_x = gallery_link_y = 500
    blog_link_x = blog_link_y = 600
    gallery_link_rot = blog_link_rot = 0
    try:
        gallery_link = GalleryLinkPosition.objects.get(is_default=True)
        gallery_link_x = gallery_link.pos_x
        gallery_link_y = gallery_link.pos_y
        gallery_link_rot = gallery_link.rotation
    except GalleryLinkPosition.DoesNotExist:
        pass
    try:
        blog_link = BlogLinkPosition.objects.get(is_default=True)
        blog_link_x = blog_link.pos_x
        blog_link_y = blog_link.pos_y
        blog_link_rot = blog_link.rotation
    except BlogLinkPosition.DoesNotExist:
        pass

    # For rendering some javascript
    link_selectors = [("link_%d"%link.id,link.rotation) for link in FlatPage.objects.all()]
    link_selectors.append(("gallery_link",gallery_link_rot))
    link_selectors.append(("blog_link",blog_link_rot))

    # Gallery preview images
    galleries = Gallery.objects.all()

    # background image
    try:
        bgimage = BackgroundImage.objects.get(use_for_mainpage=True)
    except BackgroundImage.DoesNotExist:
        pass

    # color scheme
    try:
        colorscheme = ColorScheme.objects.get(use_for_mainpage=True)
    except ColorScheme.DoesNotExist:
        pass

    return render_to_response('index.html', locals(),context_instance=RequestContext(request))

def change_links(request):
    transforms = json.loads(request.raw_post_data).get('transforms')

    if not transforms:
        return HttpResponseBadRequest(str(transforms))

    for transform in transforms:
        if transform.get("link_id") == "gallery":
            try:
                transform_me = GalleryLinkPosition.objects.get(is_default=True)
            except GalleryLinkPosition.DoesNotExist:
                transform_me = GalleryLinkPosition()
        elif transform.get("link_id") == "blog":
            try:
                transform_me = BlogLinkPosition.objects.get(is_default=True)
            except BlogLinkPosition.DoesNotExist:
                transform_me = BlogLinkPosition()
        else:
            transform_me = get_object_or_404(FlatPage, id=int(transform.get("link_id")))
                
        transform_me.pos_x = transform.get("left")
        transform_me.pos_y = transform.get("top")
        transform_me.rotation = transform.get("angle")
        transform_me.save()

    return HttpResponse("")

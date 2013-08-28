from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from paypal.standard.forms import PayPalPaymentsForm
from galleries.utils import random_string
from galleries import models
from settings.models import BackgroundImage, ColorScheme

def get_prefs(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        try:
            colorscheme = prefs.ColorScheme.objects.get(use_for_galleries=True)
        except prefs.ColorScheme.DoesNotExist:
            colorscheme = None
        try:
            bgimage = prefs.BackgroundImage.objects.get(use_for_galleries=True)
        except prefs.BackgroundImage.DoesNotExist:
            bgimage = None
        return view(request, colorscheme, bgimage, *args, **kwargs)
    return wrapper

@get_prefs
def galleries_index(request):
    all_galleries = models.Gallery.objects.all()

    return render_to_response("galleries_index.html", locals(), context_instance=RequestContext(request, locals()))

@get_prefs
def galleries_show(request, gallery):
    # Background image
    try:
        bgimage = BackgroundImage.objects.get(use_for_galleries=True)
    except BackgroundImage.DoesNotExist:
        pass

    # color scheme
    try:
        colorscheme = ColorScheme.objects.get(use_for_galleries=True)
    except ColorScheme.DoesNotExist:
        pass

    gallery = get_object_or_404(models.Gallery, title_slug=gallery)
    all_images = gallery.image_set.all()
    colorscheme = gallery.colorscheme
    return render_to_response("galleries_show.html", locals(), context_instance=RequestContext(request, locals()))

@get_prefs
def image_show(request, image):
    # Background image
    try:
        bgimage = BackgroundImage.objects.get(use_for_galleries=True)
    except BackgroundImage.DoesNotExist:
        pass

    # color scheme
    try:
        colorscheme = ColorScheme.objects.get(use_for_galleries=True)
    except ColorScheme.DoesNotExist:
        pass

    image = get_object_or_404(models.Image, title_slug=image)
    gallery = image.gallery

    # Paypal form info
    mysite = Site.objects.get_current()
    domain = mysite.domain
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": image.price,
        "item_name": image.title,
        "item_number": image.id,
        "no_shipping": PayPalPaymentsForm.SHIPPING_CHOICES[1][0],
        "invoice": random_string(),
        "notify_url": "http://%s%s"%(domain, reverse('paypal-ipn')),
        "return_url": "http://%s%s"%(domain, reverse("purchase_return",args=(image.title_slug,))),
        "cancel_return": "http://%s%s"%(domain, reverse("purchase_cancel",args=(image.title_slug,)))
    }
    the_form = PayPalPaymentsForm(initial=paypal_dict)

    # Change this in production!
    form = the_form.sandbox()

    # Use gallery colorscheme
    try:
        colorscheme = ColorScheme.objects.get(use_for_galleries=True)
    except ColorScheme.DoesNotExist:
        pass
        
    return render_to_response("image_show.html", locals(), context_instance=RequestContext(request))

@csrf_exempt
def purchase_return(request, image):
    image = get_object_or_404(models.Image, title_slug=image.title_slug)
    messages.add_message(request, messages.SUCCESS, "Your purchase of %s was been completed."%image.title)
    return redirect("image_show", image.title_slug)

@csrf_exempt
def purchase_cancel(request, image):
    image = get_object_or_404(models.Image, title_slug=image.title_slug)
    messages.add_message(request, messages.ERROR, "Your purchase of %s was cancelled."%image.title)
    return redirect("image_show", image.title_slug)

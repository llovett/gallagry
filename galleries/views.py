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

def galleries_index(request):
    all_galleries = models.Gallery.objects.all()

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

    return render_to_response("galleries_index.html", locals(), context_instance=RequestContext(request, locals()))

def galleries_show(request, gallery_id):
    gallery = get_object_or_404(models.Gallery,id=gallery_id)
    all_images = gallery.image_set.all()
    colorscheme = gallery.colorscheme
    return render_to_response("galleries_show.html", locals(), context_instance=RequestContext(request, locals()))

@ensure_csrf_cookie
def image_show(request, gallery_id, image_id):
    gallery = get_object_or_404(models.Gallery, id=gallery_id)
    image = get_object_or_404(models.Image, id=image_id)

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
        "return_url": "http://%s%s"%(domain, reverse("purchase_return",args=(gallery.id,image_id,))),
        "cancel_return": "http://%s%s"%(domain, reverse("purchase_cancel",args=(gallery.id,image_id,)))
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
def purchase_return(request, gallery_id, image_id):
    image = get_object_or_404(models.Image, id=image_id)
    messages.add_message(request, messages.SUCCESS, "Your purchase of %s was been completed."%image.title)
    return redirect("image_show", gallery_id, image_id)

@csrf_exempt
def purchase_cancel(request, gallery_id, image_id):
    image = get_object_or_404(models.Image, id=image_id)
    messages.add_message(request, messages.ERROR, "Your purchase of %s was cancelled."%image.title)
    return redirect("image_show", gallery_id, image_id)

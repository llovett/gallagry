from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from galleries.utils import random_string
from galleries import models

def galleries_index(request):
    all_galleries = models.Gallery.objects.all()
    return render_to_response("galleries_index.html", locals(), context_instance=RequestContext(request))

def galleries_show(request, gallery_id):
    gallery = get_object_or_404(models.Gallery,id=gallery_id)
    all_images = get_list_or_404(models.Image, gallery=gallery)
    return render_to_response("galleries_show.html", locals(), context_instance=RequestContext(request))

def image_show(request, gallery_id, image_id):
    gallery = get_object_or_404(models.Gallery, id=gallery_id)
    image = get_object_or_404(models.Image, id=image_id)

    # Paypal form info
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": image.price,
        "item_name": image.title,
        "invoice": random_string(),
        "notify_url": reverse("purchase_notify",args=(image_id,)),
        "return_url": reverse("purchase_return",args=(image_id,)),
        "cancel_return": reverse("purchase_cancel",args=(image_id,))
    }
    form = PayPalPaymentsForm(initial=paypal_dict)

    return render_to_response("image_show.html", locals(), context_instance=RequestContext(request))

def purchase_notify(request, gallery_id, image_id):
    image = get_object_or_404(models.ImageFrame, id=image_id)
    messages.add_message(request, messages.SUCCESS, "Your purchase of %s has been completed."%image.title)
    
    # Art has been sold, so not for sale anymore
    image.for_sale = False
    image.save()

    return reverse("image_detail", args=(image_id,))

def purchase_return(request, gallery_id, image_id):
    image = get_object_or_404(models.Image, id=image_id)
    messages.add_message(request, messages.ERROR, "Your purchase of %s was cancelled."%image.title)
    return reverse("image_detail", args=(image_id,))

def purchase_cancel(request, gallery_id, image_id):
    image = get_object_or_404(models.Image, id=image_id)
    messages.add_message(request, messages.ERROR, "Your purchase of %s was cancelled."%image.title)
    return reverse("image_detail", args=(image_id,))

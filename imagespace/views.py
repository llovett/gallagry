from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.conf import settings
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
from imagespace import models
from imagespace.utils import random_string

def main_page(request):
    images = get_list_or_404(models.ImageFrame, visible=True)
    return render_to_response('index.html', locals(),context_instance=RequestContext(request))

def image_detail(request, image_id):
    image = get_object_or_404(models.ImageFrame, id=image_id)

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
    
    return render_to_response("image_detail.html", locals(), context_instance=RequestContext(request))

def purchase_notify(request, image_id):
    image = get_object_or_404(models.ImageFrame, id=image_id)
    messages.add_message(request, messages.SUCCESS, "Your purchase of %s has been completed."%image.title)
    return reverse("image_detail", args=(image_id,))

def purchase_return(request, image_id):
    image = get_object_or_404(models.ImageFrame, id=image_id)
    messages.add_message(request, messages.ERROR, "Your purchase of %s was cancelled."%image.title)
    return reverse("image_detail", args=(image_id,))

def purchase_cancel(request, image_id):
    image = get_object_or_404(models.ImageFrame, id=image_id)
    messages.add_message(request, messages.ERROR, "Your purchase of %s was cancelled."%image.title)
    return reverse("image_detail", args=(image_id,))

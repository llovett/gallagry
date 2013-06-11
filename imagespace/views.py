from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from imagespace import models

def main_page(request):
    images = get_list_or_404(models.ImageFrame, visible=True)
    return render_to_response('index.html', locals(),context_instance=RequestContext(request))

def image_detail(request, image_id):
    image = get_object_or_404(models.ImageFrame, id=image_id)

    # Paypal form info
    # paypal_dict = {
    #     "business": "yourpaypalemail@example.com",
    #     "amount": "10000000.00",
    #     "item_name": "name of the item",
    #     "invoice": "unique-invoice-id",
    #     "notify_url": "http://www.example.com/your-ipn-location/",
    #     "return_url": "http://www.example.com/your-return-location/",
    #     "cancel_return": "http://www.example.com/your-cancel-location/",
    # }

    return render_to_response("image_detail.html", locals(), context_instance=RequestContext(request))

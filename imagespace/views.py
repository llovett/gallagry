from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from imagespace import models

def main_page(request):
    images = get_list_or_404(models.ImageFrame, visible=True)
    return render_to_response('index.html', locals(),context_instance=RequestContext(request))



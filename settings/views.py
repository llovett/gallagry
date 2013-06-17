from django.http import HttpResponse

def set_resolution(request, width, height):
    request.session["resolution"] = "%dx%d"%(int(width), int(height))
    return HttpResponse("")

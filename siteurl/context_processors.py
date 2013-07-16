from django.contrib.sites.models import Site

def sites(request):
    ''' Adds current Site to the template context. '''
    return {'SITE':Site.objects.get_current()}

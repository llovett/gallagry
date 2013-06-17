from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'settings.views',

    # Sets screen resolution in the session
    url(r'^resolution/([0-9]+)/([0-9]+)$', 'set_resolution', name='set_resolution'),
)

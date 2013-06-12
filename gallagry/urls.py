from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import redirect_to
import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^art/', include('imagespace.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),

    # Default page redirects to gallery
    url(r'^$', redirect_to, {'url':'/art/'}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

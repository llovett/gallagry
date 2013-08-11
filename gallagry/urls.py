from django.conf.urls import patterns, include, url
from django.contrib import admin
from myadmin.sites import MyAdminSite
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from frontpage import views
import settings

admin.site = MyAdminSite()
admin.autodiscover()

# Getting rid of some stuff in the admin site
from django.contrib.auth.models import User, Group
#from paypal.standard.ipn.models import PayPalIPN
from django.contrib.sites.models import Site
from tagging.models import Tag, TaggedItem
admin.site.unregister(User)
admin.site.unregister(Group)
#admin.site.unregister(PayPalIPN)
admin.site.unregister(Site)
admin.site.unregister(Tag)
admin.site.unregister(TaggedItem)

urlpatterns = patterns(
    '',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', views.main_page, name="main_page"),
    url(r'^edit/$', views.change_links, name="change_links"),
    url(r'^galleries/', include('galleries.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^settings/', include('settings.urls')),

    # TinyMCE stuff:
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),

    # Blog stuff:
    url(r'^news/', include('barebones.urls')),

    # Paypal
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns(
    '',
    (r'^pay/for/art/', include('paypal.standard.ipn.urls')),
)

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'galleries.views',

    url(r'^$', 'galleries_index', name='galleries_index'),
    url(r'^([0-9]+)$', 'galleries_show', name="galleries_show"),
    url(r'^([0-9]+)/([0-9]+)$', 'image_show', name='image_show'),
#    url(r'^([0-9]+)/([0-9]+)/complete$', 'purchase_notify', name="purchase_notify"),
    url(r'^([0-9]+)/([0-9]+)/return$', 'purchase_return', name="purchase_return"),
    url(r'^([0-9]+)/([0-9]+)/cancel$', 'purchase_cancel', name="purchase_cancel"),
)

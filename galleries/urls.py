from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'galleries.views',

    url(r'^galleries$', 'galleries_index', name='galleries_index'),
    url(r'^galleries/([^/]+)$', 'galleries_show', name="galleries_show"),
    url(r'^images/([^/]+)$', 'image_show', name='image_show'),
    url(r'^images/([^/]+)/complete$', 'purchase_return', name="purchase_return"),
    url(r'^images/([^/]+)/cancel$', 'purchase_cancel', name="purchase_cancel"),
)

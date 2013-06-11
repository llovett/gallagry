from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'imagespace.views',

    url(r'^$', 'main_page', name='main_page'),
    url(r'^([0-9]+)$', 'image_detail', name="image_detail"),
    url(r'^([0-9]+)/complete$', 'purchase_notify', name="purchase_notify"),
    url(r'^([0-9]+)/return$', 'purchase_return', name="purchase_return"),
    url(r'^([0-9]+)/cancel$', 'purchase_cancel', name="purchase_cancel"),
)

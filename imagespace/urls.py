from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'imagespace.views',

    url(r'^$', 'main_page', name='main_page'),
)

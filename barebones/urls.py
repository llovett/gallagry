from django.conf.urls import patterns, include, url
from django.contrib import admin
from barebones import views

admin.autodiscover()

urlpatterns = patterns(
    'barebones.views',
    
    url(r'^$', 'main_page', name="news_main"),
    url(r'^tags/([-_a-zA-Z0-9]+)$', 'get_tagged', name="get_tagged"),
    url(r'^post/([-_a-zA-Z0-9]+)$', 'get_post', name="get_post"),
)

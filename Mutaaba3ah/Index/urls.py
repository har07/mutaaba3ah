from django.conf.urls import patterns, include, url
from Index.views import main_page, sign_post

urlpatterns = patterns('',
    url(r'^sign/$', sign_post),
    url(r'^$', main_page),
)
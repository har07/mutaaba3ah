"""
Definition of urls for DjangoCore.
"""

from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('Index.urls')),
    # Examples:
    # url(r'^$', 'DjangoCore.views.home', name='home'),
    # url(r'^DjangoCore/', include('DjangoCore.DjangoCore.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

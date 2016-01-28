from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scaffold.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',  TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^login/$', 'scaffold.views.login', name='login'),
    url(r'^logout/$', 'scaffold.views.logout', name='logout'),
    url(r'^mutaaba3ah/', include('mutaaba3ah.urls')),
    # url(r'^mutaaba3ah/', TemplateView.as_view(template_name="index.html"), name='mutaaba3ah'),

    url(r'^_ah/', include('djangae.urls')),

    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^csp/', include('cspreports.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),
)

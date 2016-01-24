from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('mutaaba3ah.views',
    url(r'^$', TemplateView.as_view(template_name="mutaaba3ah/index.html"), name='mutaaba3ah'),
    url(r'^soon/$', TemplateView.as_view(template_name="mutaaba3ah/soon.html"), name='soon'),
)
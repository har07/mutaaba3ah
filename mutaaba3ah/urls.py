from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('mutaaba3ah.views',
    # url(r'^$', TemplateView.as_view(template_name="mutaaba3ah/index.html"), name='mutaaba3ah'),
    url(r'^$', 'current_month_entries', name='mutaaba3ah'),
    url(r'^add/$', 'add_or_edit_entry', name='mutaaba3ah/add'),
    url(r'^delete/(?P<id>\d+[lL]*)$', 'delete_entry', name='mutaaba3ah/delete'),
    url(r'^edit/(?P<id>\d+[lL]*)$', 'add_or_edit_entry', name='mutaaba3ah/edit'),
    url(r'^(?P<id>\d+[lL]*)$', 'display_entry', name='mutaaba3ah/display'),
    url(r'^report/$', 'report', name='mutaaba3ah/report'),
    url(r'^soon/$', TemplateView.as_view(template_name="mutaaba3ah/soon.html"), name='soon'),
)
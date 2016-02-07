from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('mutaaba3ah.views',
    # url(r'^$', TemplateView.as_view(template_name="mutaaba3ah/index.html"), name='mutaaba3ah'),
    # url(r'^$', 'current_month_entries', name='mutaaba3ah'),
    url(r'^$', 'add_or_edit_entry', name='mutaaba3ah'),
    url(r'^delete/(?P<id>\d+[lL]*)$', 'delete_entry', name='mutaaba3ah/delete'),
    url(r'^edit/(?P<id>\d+[lL]*)$', 'add_or_edit_entry', name='mutaaba3ah/edit'),
    url(r'^(?P<id>\d+[lL]*)$', 'display_entry', name='mutaaba3ah/display'),
    url(r'^report/$', 'report', name='mutaaba3ah/report'),
    url(r'^report/get_report_content/(?P<date_from>\d*)/(?P<date_to>\d*)$', 'get_report_content', name='mutaaba3ah/get_report_content'),
    url(r'^soon/$', TemplateView.as_view(template_name="mutaaba3ah/soon.html"), name='soon'),
)
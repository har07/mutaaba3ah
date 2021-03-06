from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    'mutaaba3ah.views',
    url(r'^$', 'add_or_edit_entry', name='mutaaba3ah'),
    url(r'^delete/(?P<id>\d+[lL]*)$', 'delete_entry', name='mutaaba3ah/delete'),
    url(r'^edit/(?P<id>\d+[lL]*)$', 'add_or_edit_entry', name='mutaaba3ah/edit'),
    url(r'^(?P<id>\d+[lL]*)$', 'display_entry', name='mutaaba3ah/display'),
    url(r'^report/$', 'report', name='mutaaba3ah/report'),
    url(r'^report/get_report_content/(?P<date_from>\d*)/(?P<date_to>\d*)$', 'get_report_content', name='mutaaba3ah/get_report_content'),
    url(r'^weekly_report/$', 'weekly_report', name='mutaaba3ah/weekly'),
    url(r'^weekly_report/data$', 'get_weekly_report_data', name='mutaaba3ah/weekly_data'),
    url(r'^daily_report/$', 'daily_report', name='mutaaba3ah/daily'),
    url(r'^daily_report/data$', 'get_daily_report_data', name='mutaaba3ah/daily_data'),
)
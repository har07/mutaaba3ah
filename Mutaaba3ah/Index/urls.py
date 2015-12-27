from django.conf.urls import patterns, include, url
from Index.views import main_page, get_report_data, report_page, save_report

urlpatterns = patterns('',
    url(r'^report/$', report_page),
    url(r'^get_report_data/$', get_report_data),
    url(r'^save_report/$', save_report),
    url(r'^$', main_page),
)
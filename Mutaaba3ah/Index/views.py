from django.http import HttpResponseRedirect, HttpResponse
#from django.views.generic import TemplateView
from django.shortcuts import render
from google.appengine.api import users
import urllib
import json

from Index.models import *
from Index import form_helper as fh

def main_page(request):
    mutaaba3ah_name = request.GET.get('mutaaba3ah_name', MUTAABA3AH_NAME)
    template_values = fh.get_new_laporan_model(request)
    return render(request, 'mutaaba3ah/form.html', template_values)

def save_report(request):
    if request.method == "POST":
        laporan = Laporan()
        laporan.user = users.get_current_user()
        fh.fill_laporan_from_post(laporan, request)

        laporan.put()
    template_values = fh.get_new_laporan_model(request, isSuccess=True, sucessDate=laporan.created_date)
    return render(request, 'mutaaba3ah/form.html', template_values)

def sample_method(request):
    mutaaba3ah_name = request.GET.get('mutaaba3ah_name', MUTAABA3AH_NAME)

    # Ancestor Queries, as shown here, are strongly consistent with the High
    # Replication Datastore. Queries that span entity groups are eventually
    # consistent. If we omitted the ancestor from this query there would be
    # a slight chance that Greeting that had just been written would not
    # show up in a query.
    greetings_query = Greeting.query(ancestor=mutaaba3ah_key(mutaaba3ah_name))
    greetings = greetings_query.fetch(10)

    if users.get_current_user():
        url = users.create_logout_url(request.get_full_path())
        url_linktext = 'Logout'
    else:
        url = users.create_login_url(request.get_full_path())
        url_linktext = 'Login'

    template_values = {
        'greetings': greetings,
        'mutaaba3ah_name': mutaaba3ah_name,
        'url': url,
        'url_linktext': url_linktext
    }

    #return direct_to_template(request, 'guestbook/main_page.html')
    #return TemplateView.as_view(template_name='guestbook/main_page.html')
    #return HttpResponse('<h1>Page was found</h1>')
    return render(request, 'mutaaba3ah/main_page.html', template_values)

def get_report_data(request):
    mutaaba3ah_name = request.GET.get('mutaaba3ah_name', MUTAABA3AH_NAME)

    # Ancestor Queries, as shown here, are strongly consistent with the High
    # Replication Datastore. Queries that span entity groups are eventually
    # consistent. If we omitted the ancestor from this query there would be
    # a slight chance that Greeting that had just been written would not
    # show up in a query.
    query = Laporan.query(ancestor=mutaaba3ah_key(mutaaba3ah_name))
    #laporans = query.fetch(50)
    laporans = query.fetch()
    laporans_json = json.dumps([p.to_dict() for p in laporans])
    return HttpResponse(laporans_json, content_type='application/json')

#TODO: report = report mutaba'ah selama bulan ini
def report_page(request):
    template_values = {
        'laporans': laporan
    }
    return render(request, 'mutaaba3ah/report.html', template_values)
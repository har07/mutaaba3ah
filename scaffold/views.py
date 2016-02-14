from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from google.appengine.api import users

def login(request):
    """Redirects to the Google App Engine authentication page."""

    url = users.create_login_url(dest_url=request.GET.get('next'))
    return HttpResponseRedirect(url)

def logout(request):
    """Redirects to the homepage after logging the user out."""

    url = users.create_logout_url(reverse('mutaaba3ah'))
    return HttpResponseRedirect(url)

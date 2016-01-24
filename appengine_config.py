import os

#monkey patch to avoid error "ImportError: No module named msvcrt"
#ref: http://stackoverflow.com/questions/25915164/django-1-7-on-app-engine-importerror-no-module-named-msvcrt
on_appengine = os.environ.get('SERVER_SOFTWARE','').startswith('Development')
if on_appengine and os.name == 'nt':
    os.name = None
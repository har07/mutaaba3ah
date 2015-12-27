from Index.models import *
from google.appengine.api import users
import datetime
import json

def fill_laporan_from_post(laporan, request):
    jsonData = request.POST.get("formData","")
    object = json.loads(jsonData)
    test = json.loads(request.POST)
    #laporan.date = convert_value(request.POST.get("tanggal",None), datetime.date)
    laporan.tilawah_start = convert_value(request.POST.get("tilawah",None), int)
    laporan.tilawah_end = convert_value(request.POST.get("tilawah_to",None), int)
    laporan.tilawah_start = convert_value(request.POST.get("tilawah",None), int)
    laporan.ql = convert_value(request.POST.get("ql",None), int)
    laporan.dhuha = convert_value(request.POST.get("dhuha",None), int)
    if request.POST.get("shaum",None) == "1":
        laporan.shaum = True
    else:
        laporan.shaum = False
    return laporan

def convert_value(raw, type):
    try:
        result = type(raw)
    except ValueError:
        if type == int:
            return 0
        if type == bool:
            return False
        #if type == datetime.date:
        #    return datetime.date(
    return result

def get_new_laporan_model(request, isSuccess=False, sucessDate=None):
    laporan = Laporan()
    
    if users.get_current_user():
        url = users.create_logout_url(request.get_full_path())
        url_linktext = 'Logout'
        isLoggedin = True
        laporan.user = users.get_current_user()
    else:
        url = users.create_login_url(request.get_full_path())
        url_linktext = 'Login'
        isLoggedin = False

    template_values = {
        'url': url,
        'url_linktext': url_linktext,
        'isLoggedin': isLoggedin,
        'laporan': laporan
    }

    template_values['isSuccess'] = isSuccess
    template_values['saved_date'] = sucessDate

    return template_values
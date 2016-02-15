import datetime
from collections import defaultdict

from models import Entry


DATE_FORMAT = '%Y%m%d'

def get_current_month_data(user, date):
    now = date
    last_day_prev_month = datetime.date(now.year,now.month,1)  - datetime.timedelta(days=1)
    data = Entry.objects.filter(owner=user,
                                entry_date__gt=last_day_prev_month,
                                entry_date__lte=now.date())
    return data

def get_date_from_string(datestring):
    date_object = datetime.datetime.strptime(datestring, DATE_FORMAT)
    return date_object

def get_last_sunday(date=datetime.datetime.today().date()):
    """
    Get previous sunday date nearest to the date parameter
    :param date:
    :return:
    """
    if date.weekday() == 6:
        return date
    return date - datetime.timedelta(days=date.weekday()+1)

def group_entries_weekly(entries):
    """
    Turn list of daily mutaba'ah entries
    into dictionary of 'sunday date' : 'weekly aggregate'
    :param entries:
    :return:
    """
    d = defaultdict(list)
    for entry in entries:
        d[get_last_sunday(entry.entry_date)].append(entry)

    result = {
        k: {
            'date_from': k,
            'date_to': k + datetime.timedelta(days=6),
            'tilawah': sum(entry.compute_tilawah() for entry in v),
            'ql': sum(entry.ql for entry in v),
            'dhuha': sum(entry.dhuha for entry in v),
            'shaum': sum(1 for entry in v if entry.shaum),
            'raport': sum(1 for entry in v if entry.raport),
        }
        for (k,v) in d.iteritems()
    }

    return result
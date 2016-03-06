import datetime
from collections import defaultdict

from models import Entry


DATE_FORMAT = '%Y%m%d'
DISPLAY_DATE_FORMAT = '%d %b %Y'
DISPLAY_DATE_NO_YEAR = '%d %b'

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

def get_date_range_label(date_from, date_to):
    if date_from.year == date_to.year and date_from.month == date_to.month \
            and date_from.day == date_to.day:
        return date_to.strftime(DISPLAY_DATE_NO_YEAR)
    elif date_from.year == date_to.year and date_from.month == date_to.month:
        return format(date_from.day, '02d') + ' - ' + (date_to.strftime(DISPLAY_DATE_NO_YEAR))

    return (date_from.strftime(DISPLAY_DATE_NO_YEAR)) + ' - ' + (date_to.strftime(DISPLAY_DATE_NO_YEAR))

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

    result = [
        {
            'label': get_date_range_label(k, (k + datetime.timedelta(days=6))),
            'date_from': k,
            'date_to': k + datetime.timedelta(days=6),
            'tilawah': sum(entry.compute_tilawah() for entry in v),
            'ql': sum(entry.ql for entry in v),
            'dhuha': sum(entry.dhuha for entry in v),
            'shaum': sum(1 for entry in v if entry.shaum),
            'raport': 7-sum(1 for entry in v if entry.raport),
        }
        for (k,v) in d.iteritems()
    ]

    sorted_result = sorted(result, key=lambda k: k['date_to'])
    return sorted_result


def format_daily_entries(entries):
    """
    Turn plain list of daily mutaba'ah entries
    into dictionary ready for display in chart
    :param entries:
    :return:
    """

    result = [
        {
            # display full date label for 1st date of a month
            'label': e.entry_date.strftime(DISPLAY_DATE_NO_YEAR) \
                        if e.entry_date.day == 1 \
                     else e.entry_date.day,
            'date': e.entry_date,
            'tilawah': e.compute_tilawah(),
            'ql': e.ql,
            'dhuha': e.dhuha,
            'shaum': 1 if e.shaum else 0,
            'raport': 1 if not e.raport else 0,
        }
        for e in entries
    ]

    # display full date label for the 1st entry
    if result:
        result[0]['label'] = result[0]['date'].strftime(DISPLAY_DATE_NO_YEAR)

    return result
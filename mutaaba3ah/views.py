from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse

import datetime

from models import Entry
from forms import EntryForm, DeleteEntryForm
from helpers import get_date_from_string, get_current_month_data, \
    group_entries_weekly, format_daily_entries

#region application page methods


@login_required()
def add_or_edit_entry(request, id=None):

    if id:
        entry = get_object_or_404(Entry, id=id)
    else:
        entry = Entry()

    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('mutaaba3ah/display',
                                                kwargs={'id': new_entry.id}))

    else:
        form = EntryForm(instance=entry)

    data = {'form': form, 'is_new': bool(id)}
    return render(request, 'mutaaba3ah/create_or_edit_entry.html', data)


@login_required()
def display_entry(request, id):
    entry = get_object_or_404(Entry, id=id)

    data = {
        'form': entry,
    }

    return render(request, 'mutaaba3ah/display_entry.html', data)


@login_required()
def report(request):
    now = datetime.datetime.now()
    data = {
        'entries': get_current_month_data(request.user, now)
    }
    return render(request, 'mutaaba3ah/report.html', data)


@login_required()
def delete_entry(request, id):
    """
    Renders a form to support the deletion of existing Entry objects.

    Using a form allows us to protect against CSRF attacks.
    """

    entry = get_object_or_404(Entry, id=id)

    if request.method == 'POST':
        form = DeleteEntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry.delete()
            return HttpResponseRedirect(reverse('mutaaba3ah'))
    else:
        form = DeleteEntryForm(instance=entry)

    data = {'form': form, 'entry': entry}
    return render(request, 'mutaaba3ah/delete_entry.html', data)


@login_required()
def weekly_report(request):
    data = {}
    return render(request, 'mutaaba3ah/weekly_report.html', data)
    # return render(request, 'mutaaba3ah/line.html', data)


@login_required()
def daily_report(request):
    data = {}
    return render(request, 'mutaaba3ah/daily_report.html', data)


#endregion


#region AJAX methods


@login_required()
def get_report_content(request, date_from=None, date_to=None):
    entries = []
    if date_from and date_to:
        date_from = get_date_from_string(date_from)
        date_to = get_date_from_string(date_to)
        entries = Entry.objects.filter(owner=request.user,
                                        entry_date__gte=date_from,
                                        entry_date__lte=date_to)[:100]
    elif date_to:
        date_from = get_date_from_string(date_from)
        entries = Entry.objects.filter(owner=request.user,
                                        entry_date__gte=date_from)[:100]
    elif date_from:
        date_to = get_date_from_string(date_to)
        entries = Entry.objects.filter(owner=request.user,
                                        entry_date__lte=date_to)[:100]
    else:
        entries = Entry.objects.filter(owner=request.user)[:100]

    data = {
        'entries': entries
    }
    return render(request, 'mutaaba3ah/report_content.html', data)


@login_required()
def get_weekly_report_data(request):
    """
    Get current year entries grouped by week
    return data as JSON
    :param request:
    :return:
    """
    year_start = datetime.date(datetime.date.today().year,1,1)
    entries = Entry.objects.filter(owner=request.user,
                                        entry_date__gte=year_start)[:366]
    grouped_entries = group_entries_weekly(entries)
    return JsonResponse(grouped_entries, safe=False)


@login_required()
def get_daily_report_data(request):
    year_start = datetime.date(datetime.date.today().year,1,1)
    entries = Entry.objects.filter(owner=request.user,
                                        entry_date__gte=year_start)[:366]
    return JsonResponse(format_daily_entries(entries), safe=False)


#endregion


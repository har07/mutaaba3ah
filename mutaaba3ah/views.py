from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import datetime

from models import Entry
from forms import EntryForm, DeleteEntryForm


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
def current_month_entries(request):
    now = datetime.datetime.now()
    current_month_year =now.strftime('%B %Y')
    last_day_prev_month = datetime.date(now.year,now.month,1)  - datetime.timedelta(days=1)

    data = {
        'entries': Entry.objects.filter(owner=request.user,
                                        entry_date__gt=last_day_prev_month,
                                        entry_date__lte=now.date()),
        'current_month_year': current_month_year,
    }
    return render(request, 'mutaaba3ah/index.html', data)


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

    data = {'form': form}
    return render(request, 'mutaaba3ah/delete_entry.html', data)
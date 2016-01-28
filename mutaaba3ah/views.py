from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Entry
from forms import EntryForm

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

    data = {'form': form}
    return render(request, 'mutaaba3ah/create_or_edit_entry.html', data)

@login_required()
def display_entry(request, id):
    entry = get_object_or_404(Entry, id=id)

    data = {
        'form': entry,
    }

    return render(request, 'mutaaba3ah/create_or_edit_entry.html', data)

@login_required()
def current_month_entries(request):
    pass
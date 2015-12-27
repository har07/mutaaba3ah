from django import forms
import datetime

class LaporanForm(forms.Form):
    created_date = forms.DateField(initial=datetime.date.today)
    tanggal = forms.DateField()
    tilawah_start = forms.IntegerField(max_value=604, min_value=0)
    tilawah_end = forms.IntegerField(max_value=604, min_value=0)
    ql = forms.IntegerField(min_value=0)
    dhuha = forms.IntegerField(min_value=0)
    shaum = forms.BooleanField()
    raport = forms.BooleanField()
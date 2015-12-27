from django import forms
import datetime

class LaporanForm(forms.Form):
    created_date = forms.DateField(initial=datetime.date.today)
    tanggal = forms.DateField()
    tilawah_start = forms.IntegerField(required=False,max_value=604, min_value=0)
    tilawah_end = forms.IntegerField(required=False,max_value=604, min_value=0)
    ql = forms.IntegerField(required=False,min_value=0)
    dhuha = forms.IntegerField(required=False,min_value=0)
    shaum = forms.BooleanField(required=False,)
    raport = forms.BooleanField(required=False,)

    def clean(self):
        cleaned_data = super(LaporanForm, self).clean()
        non_empty_counter = 0
        min_non_empty = 3 #crated_date, tanggal, ditambah minimal 1 field lagi yg harus terisi
        for field_value in cleaned_data.itervalues():
            # Check for None or '', so IntegerFields with 0 or similar things don't seem empty.
            if field_value is not None and field_value != '':
                non_empty_counter += 1
        if non_empty_counter < min_non_empty:
            raise forms.ValidationError("You must fill at least one field!")
        return cleaned_data   # Important that clean should return cleaned_data!
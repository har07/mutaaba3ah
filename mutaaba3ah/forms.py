from django import forms

from models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['entry_date', 'tilawah_start', 'tilawah_end', 'ql', 'dhuha', 'shaum', 'raport']
        widgets = {
            'entry_date': forms.DateInput(attrs={
                'placeholder': 'Tanggal',
                'class': 'form-control datepicker',
                # 'readonly': 'readonly',
                'title': 'Tanggal',
            }),
            'tilawah_start': forms.NumberInput(attrs={
                'placeholder': 'Halaman mulai',
                'class': 'form-control',
                'title': 'Halaman mulai'
            }),
            'tilawah_end': forms.NumberInput(attrs={
                'placeholder': 'Halaman selesai',
                'class': 'form-control',
                'title': 'Halaman selesai'
            }),
            'ql': forms.NumberInput(attrs={
                'placeholder': 'Qiyamul Lail',
                'class': 'form-control',
                'aria-describedby': 'raka3at1',
                'title': 'Qiyamullail'
            }),
            'dhuha': forms.NumberInput(attrs={
                'placeholder': 'Dhuha',
                'class': 'form-control',
                'aria-describedby': 'raka3at2',
                'title': 'Dhuha'
            }),
            'shaum': forms.RadioSelect(attrs={
                'placeholder': 'Shaum',
                'title': 'Qiyamullail'
            }),
            'raport': forms.RadioSelect(attrs={
                'placeholder': 'Raport',
                'title': 'Raport'
            })
        }

class DeleteEntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = []

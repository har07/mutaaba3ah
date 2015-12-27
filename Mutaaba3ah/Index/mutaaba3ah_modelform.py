from django.forms import ModelForm
from Index.models import Laporan

class LaporanForm(Laporan):
    class Meta:
        model = Laporan
        fields = ['tilawah_start','tilawah_end']
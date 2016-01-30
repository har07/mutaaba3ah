from django.conf import settings
from django.db import models
import datetime

MAX_HAL_ALQURAN = 604

class Entry(models.Model):
    """Define mutaba'ah entry of a user on a certain day"""

    class Meta:
        ordering = ['entry_date']

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    #TODO: hapus " - datetime.timedelta(days=30)" sebelum di deploy
    entry_date = models.DateField(default=datetime.datetime.today() - datetime.timedelta(days=30))

    #tilawah
    tilawah_start = models.IntegerField(blank=True)
    tilawah_end = models.IntegerField(blank=True)

     #Qiyamul Lail
    ql = models.IntegerField(blank=True, default=0)

    #Dhuha
    dhuha = models.IntegerField(blank=True, default=0)

    BOOL_CHOICES = ((True, 'Iya'), (False, 'Tidak'))
    #Shaum
    shaum = models.BooleanField(blank=True, default=False, choices=BOOL_CHOICES)

    #Raport
    raport = models.BooleanField(blank=True, default=False, choices=BOOL_CHOICES)

    def compute_tilawah(self):
        if self.tilawah_end < self.tilawah_start:
            return (MAX_HAL_ALQURAN + 1 - self.tilawah_start) + self.tilawah_end

        return self.tilawah_end - self.tilawah_start + 1

    def boolean_to_text(self, value):
        if value:
            return 'Iya'
        return 'Tidak'

    def raka3at_to_text(self, value):
        if value > 0:
            return str(value) + " raka'at"
        return "-"

    def display_shaum(self):
        return self.boolean_to_text(self.shaum)

    def display_dhuha(self):
        return self.raka3at_to_text(self.dhuha)

    def display_ql(self):
        return self.raka3at_to_text(self.ql)

    def display_tilawah(self):
        if self.compute_tilawah() > 0:
            return str.format("{0} - {1}, total {2} halaman", \
                          str(self.tilawah_start), str(self.tilawah_end), \
                          str(self.compute_tilawah()))

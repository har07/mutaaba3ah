from django.conf import settings
from django.db import models
import datetime

MAX_HAL_ALQURAN = 604

class Entry(models.Model):
    """Define mutaaba'ah entry of a user on a certain day"""

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

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    #Shaum
    shaum = models.BooleanField(blank=True, default=False, choices=BOOL_CHOICES)

    #Raport
    raport = models.BooleanField(blank=True, default=False, choices=BOOL_CHOICES)

    def compute_tilawah(self):
        if self.tilawah_end < self.tilawah_start:
            return (MAX_HAL_ALQURAN + 1 - self.tilawah_start) + self.tilawah_end

        return self.tilawah_end - self.tilawah_start + 1
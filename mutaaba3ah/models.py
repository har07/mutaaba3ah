from django.conf import settings
from django.db import models

MAX_HAL_ALQURAN = 604

class Entry(models.Model):
    """Define mutaaba'ah entry of a user on certain day"""

    class Meta:
        ordering = ['-created_at']

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_date = models.DateField()

    #tilawah
    tilawah_start = models.IntegerField(blank=True, default=-1)
    tilawah_end = models.IntegerField(blank=True, default=-1)

     #Qiyamul Lail
    ql = models.IntegerField(blank=True, default=-1)

    #Dhuha
    dhuha = models.IntegerField(blank=True, default=-1)

    #Shaum
    shaum = models.BooleanField(blank=True, default=False)

    #Raport
    raport = models.BooleanField(blank=True, default=False)

    def compute_tilawah(self):
        if self.tilawah_end < self.tilawah_start:
            return (MAX_HAL_ALQURAN + 1 - self.tilawah_start) + self.tilawah_end

        return self.tilawah_end - self.tilawah_start + 1
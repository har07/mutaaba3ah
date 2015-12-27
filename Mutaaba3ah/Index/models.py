from google.appengine.ext import ndb

MUTAABA3AH_NAME = 'default_mutaaba3ah'
MAX_HAL_ALQURAN = 604

# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def mutaaba3ah_key(mutaaba3ah_name=MUTAABA3AH_NAME):
    '''Constructs a Datastore key for a Mutaaba3ah entity with mutaaba3ah_name.'''
    return ndb.Key('Mutaaba3ah', mutaaba3ah_name)

class Laporan(ndb.Model):
    '''Models an individual daily report entry.'''
    user = ndb.UserProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)

    #tanggal
    date = ndb.DateProperty()

    #tilawah
    tilawah_start = ndb.IntegerProperty()
    tilawah_end = ndb.IntegerProperty()
    tilawah = ndb.ComputedProperty(lambda self: self.compute_tilawah())
    
    #Qiyamul Lail
    ql = ndb.IntegerProperty()

    #Dhuha
    dhuha = ndb.IntegerProperty()

    #Shaum
    shaum = ndb.BooleanProperty()

    #Raport
    raport = ndb.BooleanProperty()

    def compute_tilawah(self):
        if self.tilawah_end < self.tilawah_start:
            return (MAX_HAL_ALQURAN + 1 - self.tilawah_start) + self.tilawah_end
        
        return self.tilawah_end - self.tilawah_start + 1
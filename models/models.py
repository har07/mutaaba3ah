from google.appengine.ext import db

class Entry(db.Model):
    user_name = db.StringProperty(required=True)
    user_id = db.IntegerProperty(required=True)
    date = db.DateProperty(required=True)
    dhuha = db.IntegerProperty()
    ql = db.IntegerProperty()
    tilawah_start = db.IntegerProperty()
    tilawah_end = db.IntegerProperty()
    shaum = db.BooleanProperty()

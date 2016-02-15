from google.appengine.ext import testbed

# from unittest import TestCase
from django.test import TestCase
from mutaaba3ah import helpers
from mutaaba3ah import models

import datetime


class Mutaaba3ahHelpersTest(TestCase):

    def setUp(self):
        """Initalise GAE test stubs before each test is run."""
        #
        self.testbed = testbed.Testbed()
        self.testbed.activate()

    def tearDown(self):
        """Remove the GAE test subs after each test."""
        self.testbed.deactivate()

    def test_get_last_sunday(self):
        data = {
            datetime.date(2016,2,15):datetime.date(2016,2,14),
            datetime.date(2017,12,16):datetime.date(2017,12,10),
            datetime.date(2012,1,1):datetime.date(2012,1,1),
        }
        for k,v in data.iteritems():
            self.assertEqual(helpers.get_last_sunday(k), v)

    def test_group_entries_weekly(self):
        data = []

        # data utk pekan pertama
        total_1 = {
            'date_from': datetime.date(2016,2,14),
            'date_to': datetime.date(2016,2,20),
            'tilawah': 10,
            'ql': 0,
            'dhuha': 8,
            'shaum': 1,
            'raport': 0,
        }

        e = models.Entry()
        e.entry_date = datetime.date(2016,2,15)
        e.tilawah_start = 1
        e.tilawah_end = 5
        e.dhuha = 4
        e.shaum = True
        data.append(e)

        e = models.Entry()
        e.entry_date = datetime.date(2016,2,19)
        e.tilawah_start = 0
        e.tilawah_end = 0
        e.dhuha = 4
        data.append(e)

        e = models.Entry()
        e.entry_date = datetime.date(2016,2,20)
        e.tilawah_start = 6
        e.tilawah_end = 10
        e.dhuha =0
        data.append(e)

        # data utk pekan selanjutnya
        total_2 = {
            'date_from': datetime.date(2016,2,21),
            'date_to': datetime.date(2016,2,27),
            'tilawah': 10,
            'ql': 0,
            'dhuha': 4,
            'shaum': 0,
            'raport': 1,
        }

        e = models.Entry()
        e.entry_date = datetime.date(2016,2,21)
        e.tilawah_start = 11
        e.tilawah_end = 20
        e.dhuha =4
        e.raport = True
        data.append(e)

        result = helpers.group_entries_weekly(data)
        self.assertDictEqual(result[total_1['date_from']], total_1)
        self.assertDictEqual(result[total_2['date_from']], total_2)

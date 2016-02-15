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
        start = datetime.date(2016,2,14)
        end = datetime.date(2016,2,20)
        total_1 = {
            'label': start.strftime(helpers.DISPLAY_DATE_FORMAT) + ' - ' + end.strftime(helpers.DISPLAY_DATE_FORMAT),
            'date_from': start,
            'date_to': end,
            'tilawah': 10,
            'ql': 0,
            'dhuha': 8,
            'shaum': 1,
            'raport': 0,
        }

        e = models.Entry(
            entry_date = datetime.date(2016,2,15),
            tilawah_start = 1,
            tilawah_end = 5,
            dhuha = 4,
            shaum = True
        )
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
        start = datetime.date(2016,2,21)
        end = datetime.date(2016,2,27)
        total_2 = {
            'label': start.strftime(helpers.DISPLAY_DATE_FORMAT) + ' - ' + end.strftime(helpers.DISPLAY_DATE_FORMAT),
            'date_from': start,
            'date_to': end,
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

        self.assertDictEqual(result[0], total_1)
        self.assertDictEqual(result[1], total_2)

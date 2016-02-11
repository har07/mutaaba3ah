from selenium import webdriver
import unittest
import datetime

from . import helper

class ReportTest(helper.FunctionalTestBase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.data = [{
            "dhuha": "4",
            "tilawah_from": "1",
            "tilawah_to": "20",
            "ql": "5",
            "shaum": "Iya",
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        },
        {
            "dhuha": "4",
            "tilawah_from": "1",
            "tilawah_to": "20",
            "ql": "5",
            "shaum": "Iya",
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        },
        {
            "dhuha": "4",
            "tilawah_from": "1",
            "tilawah_to": "20",
            "ql": "5",
            "shaum": "Iya",
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        }]

        # get to home page and login
        self.browser.get("http://localhost:8000")
        self.try_logout()
        self.login()

    def tearDown(self):
        self.delete_data()
        self.logout()
        self.browser.quit()
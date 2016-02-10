from selenium import webdriver
import unittest
import datetime

class ReportTest(unittest.TestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.data = {
            "dhuha": "4",
            "tilawah_from": "1",
            "tilawah_to": "20",
            "ql": "5",
            "shaum": "Iya",
            "date": datetime.datetime.now().strftime("%Y-%m-%d")
        }

    def tearDown(self):
        self.delete_data()
        self.logout()
        self.browser.quit()
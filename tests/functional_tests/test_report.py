from selenium import webdriver
import unittest
import datetime

from . import helper

class ReportTest(helper.FunctionalTestBase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        # get to home page and login
        self.browser.get("http://localhost:8000")
        self.try_logout()
        self.login()

        self.setup_data()

    def tearDown(self):
        self.cleanup_data()
        self.try_logout()
        self.browser.quit()

    def setup_data(self):
        now = datetime.date(2016, 1, 1)
        # 2 items in current week
        # 3 items in current month
        # 4 items total
        self.data = [{
            "dhuha": "4",
            "tilawah_from": "1",
            "tilawah_to": "20",
            "ql": "5",
            "shaum": "Iya",
            "date": now.strftime("%Y-%m-%d") # 2016-01-01
        },
            {
                "dhuha": "0",
                "tilawah_from": "61",
                "tilawah_to": "80",
                "ql": "5",
                "shaum": "Iya",
                "date": (now + datetime.timedelta(days=3)).strftime("%Y-%m-%d") # 2016-01-04
            },
            {
                "dhuha": "0",
                "tilawah_from": "121",
                "tilawah_to": "140",
                "ql": "5",
                "shaum": "Iya",
                "date": (now + datetime.timedelta(days=7)).strftime("%Y-%m-%d") # 2016-01-08
            },
            {
                "dhuha": "4",
                "tilawah_from": "21",
                "tilawah_to": "40",
                "ql": "5",
                "shaum": "Iya",
                "date": (now + datetime.timedelta(days=31)).strftime("%Y-%m-%d") # 2016-02-01
            }]

        # insert initial test data and move to report page
        # for data in self.data:
        #     self.navigate_to_entry()
        #     self.create_or_edit_data(data)
        self.navigate_to_report()

    def cleanup_data(self):
        for data in self.data:
            self.delete_item_by_date(data["date"])
            self.navigate_to_report()

    def test_report_data(self):
        self.assertTrue(False)
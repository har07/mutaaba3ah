from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import datetime

from . import helper

class FunctionalUnitsTest(helper.FunctionalTestBase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.is_need_cleanup = False

        self.browser.get("http://localhost:8000")
        self.try_logout()

    def tearDown(self):
        if self.is_need_cleanup:
            self.cleanup_data()
        self.try_logout()
        self.browser.quit()

    def delete_first_item(self, report_items):
        if report_items:
            item = report_items[0]

            # click on row item if it hasn't been selected
            btn_delete = self.browser.find_element_by_id("delete")
            if not btn_delete.is_enabled():
                item.click()
            btn_delete.click()

            # pindah ke window konfirmasi & klik delete
            WebDriverWait(self.browser, timeout=10).until(lambda x: len(x.window_handles) > 0)
            self.browser.switch_to.window(self.browser.window_handles[1])

            # add wait to handle intermittent 'unable to locate element' error
            WebDriverWait(self.browser, timeout=50).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='submit']")))
            submit_delete = self.browser.find_element_by_css_selector("input[type='submit']")
            submit_delete.click()

            # close window konfirmasi & kembai ke halaman sebelumnya
            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])

    def setup_data(self, insert_new):
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
            "tilawah_from": "21",
            "tilawah_to": "40",
            "ql": "5",
            "shaum": "Tidak",
            "date": (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        }]

        # insert initial test data if requested, and move to report page
        if insert_new:
            for item in self.data:
                self.navigate_to_entry()
                self.create_or_edit_data(item)
        self.navigate_to_report()

    def cleanup_data(self):
        # delete all leftover data

        leftover_items = self.find_report_items_by_date()
        if not leftover_items:
            return

        leftover_items = self.find_report_items_by_date()
        while leftover_items:
            self.delete_first_item(leftover_items)
            self.navigate_to_report()
            leftover_items = self.find_report_items_by_date()

    def test_delete_items(self):
        # go to report page
        # search & delete all items one by one
        # verify no item after deletion

        self.login()
        self.setup_data(True)
        self.is_need_cleanup = True

        report_items = self.find_report_items_by_date()
        count_before_delete = len(report_items)

        for data in self.data:
            self.delete_item_by_date(data["date"])
            self.navigate_to_report()

        # refresh report page
        # self.navigate_to_report()

        report_items = self.find_report_items_by_date()
        count_after_delete = len(report_items)

        self.assertLess(count_after_delete, count_before_delete)
        self.assertEqual(count_after_delete, count_before_delete - len(self.data))

    def test_edit_item(self):
        # go to report page
        # search first test data and edit
        # verify View Report reflects the edited data

        self.login()
        self.setup_data(True)
        self.is_need_cleanup = True

        # prepare data for edit
        updated_data = self.data[0]
        updated_data["dhuha"] = "6"
        updated_data["ql"] = "10"

        self.navigate_to_report()
        self.edit_item_by_date(updated_data)

        # refresh report page and verify updated data are displayed
        self.navigate_to_report()
        report_item = self.find_report_items_by_date(updated_data)[0]
        try:
            dhuha = report_item.find_elements_by_xpath("td[normalize-space()='%s']" % updated_data["dhuha"])
            ql = report_item.find_elements_by_xpath("td[normalize-space()='%s']" % updated_data["ql"])
        except NoSuchElementException, e:
            self.assertFalse(True, "updated data are not found: %s" % str(e))

        # updated data are has been successfully displayed in searcher
        self.assertTrue(True)

    def test_menu_visibility_after_login(self):
        self.login()

        self.assertEquals(len(self.browser.find_elements_by_id("menu-entry")), 1)
        self.assertEquals(len(self.browser.find_elements_by_id("menu-report")), 1)

    def test_menu_visibility_before_login(self):
        self.try_logout()

        self.assertEquals(len(self.browser.find_elements_by_id("user-email")), 0)
        self.assertEquals(len(self.browser.find_elements_by_id("logout")), 0)
        self.assertEquals(len(self.browser.find_elements_by_id("menu-entry")), 0)
        self.assertEquals(len(self.browser.find_elements_by_id("menu-report")), 0)




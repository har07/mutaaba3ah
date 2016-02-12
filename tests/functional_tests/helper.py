from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import unittest


class FunctionalTestBase(unittest.TestCase):
    MUTAABA3AH_PAGE_LOCATOR = "//h2[.=\"Mutaba'ah Report\"]"
    EDIT_OR_ENTRY_PAGE_LOCATOR = "//h2[.='Create a new entry' or .='Edit an existing entry']"
    DELETE_PAGE_LOCATOR = "//h2[.='Delete an entry']"


    def __init__(self, *args, **kwargs):
        self.browser = None
        unittest.TestCase.__init__(self, *args, **kwargs)


    #region login - logout

    def try_logout(self):
        try:
            self.logout()
        except NoSuchElementException:
            pass

    def login(self):
        self.validate_browser_property()

        login = self.browser.find_element_by_id("login")
        self.assertIsNotNone(login)
        login.click()
        email = self.browser.find_element_by_id("email")
        admin_login = self.browser.find_element_by_id("submit-login")
        email.clear()
        email.click()
        email.send_keys('brian@tester.com')
        admin_login.click()

    def logout(self):
        self.validate_browser_property()

        user_email = self.browser.find_element_by_id("user-email")
        user_email.click()
        logout = self.browser.find_element_by_id("logout")
        self.assertIsNotNone(logout)
        logout.click()

    #endregion

    #region data operations

    def create_or_edit_data(self, data):
        # populate Entry or Edit form with test data
        # and save

        self.validate_browser_property()
        self.validate_at_edit_or_entry_page()

        dhuha = self.browser.find_element_by_id("id_dhuha")
        dhuha.clear()
        dhuha.send_keys(data["dhuha"])
        tilawah_from = self.browser.find_element_by_id("id_tilawah_start")
        tilawah_from.clear()
        tilawah_from.send_keys(data["tilawah_from"])
        tilawah_to = self.browser.find_element_by_id("id_tilawah_end")
        tilawah_to.clear()
        tilawah_to.send_keys(data["tilawah_to"])
        ql = self.browser.find_element_by_id("id_ql")
        ql.clear()
        ql.send_keys(data["ql"])
        shaum = self.browser.find_element_by_xpath("//ul[@id='id_shaum']/li[contains(.,'%s')]" % data["shaum"])
        shaum.click()

        submit = self.browser.find_element_by_css_selector("input[type='submit']")
        submit.click()

    def edit_item_by_date(self, data):
        # get data sesuai tanggal
        # update data

        self.validate_browser_property()
        self.validate_at_report_page()

        date = data["date"]

        report_items = self.find_report_items_by_date(date)
        if report_items:
            item = report_items[0]

            # click on row item if it hasn't been selected
            btn_edit = self.browser.find_element_by_id("edit")
            if not btn_edit.is_enabled():
                item.click()
            btn_edit.click()

            # pindah ke window edit data
            WebDriverWait(self.browser, timeout=10).until(lambda x: len(x.window_handles) > 0)
            self.browser.switch_to.window(self.browser.window_handles[1])
            self.create_or_edit_data(data)

            # close window konfirmasi & kembai ke halaman sebelumnya
            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])

    def delete_item_by_date(self, date):
        # get data sesuai tanggal
        # delete data

        self.validate_browser_property()
        self.validate_at_report_page()

        report_items = self.find_report_items_by_date(date)
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

    def find_report_items_by_date(self, report_date=""):
        # search data sesuai tanggal di halaman Mutaba'ah Report
        # format report_date : yyyy-mm-dd

        self.validate_browser_property()
        self.validate_at_report_page()

        if report_date:
            date_from = self.browser.find_element_by_id("date_from")
            date_from.click()
            date_from.send_keys(report_date)

            date_from.send_keys(Keys.TAB)
            date_to = self.browser.find_element_by_id("date_to")
            date_to.send_keys(report_date)

        btn_filter = self.browser.find_element_by_id("btn-filter")
        btn_filter.click()

        items = self.browser.find_elements_by_css_selector("#mutaaba3ah-table tbody tr")
        return items

    #endregion

    #region navigation

    def navigate_to_report(self):
        menu_report = self.browser.find_element_by_id("menu-report")
        menu_mutaaba3ah = self.browser.find_element_by_id("menu-mutaaba3ah")

        if not menu_report.is_displayed():
            WebDriverWait(self.browser, 10).until(
             EC.element_to_be_clickable((By.ID, "menu-mutaaba3ah")))
            menu_mutaaba3ah.click()

        WebDriverWait(self.browser, 10).until(
             EC.element_to_be_clickable((By.ID, "menu-report")))
        menu_report.click()

        heading = WebDriverWait(self.browser, 10).until(
             EC.presence_of_element_located((By.XPATH, self.MUTAABA3AH_PAGE_LOCATOR)))

    def navigate_to_entry(self):
        menu_entry = self.browser.find_element_by_id("menu-entry")
        menu_mutaaba3ah = self.browser.find_element_by_id("menu-mutaaba3ah")
        menu_mutaaba3ah.click()
        menu_entry.click()

        heading = WebDriverWait(self.browser, 10).until(
             EC.presence_of_element_located((By.XPATH, self.EDIT_OR_ENTRY_PAGE_LOCATOR)))

    #endregion

    #region validation

    def validate_browser_property(self):
        message = "browser property hasn't been initialized: Make sure you have initialized 'self.browser' in setUp()"
        if not self.browser:
            raise RuntimeError(message)

    def validate_at_report_page(self):
        message = "Current page is not Mutaba'ah Report: call self.navigate_to_report() first"
        page_title = self.browser.find_elements_by_xpath(self.MUTAABA3AH_PAGE_LOCATOR)
        if not page_title:
            raise RuntimeError(message)

    def validate_at_edit_or_entry_page(self):
        # Create a new entry
        message = "Current page is neither Entry nor Edit page: Use self.navigate_to_entry() to go to entry page, or " \
                  + "self.navigate_to_report() + self.find_report_items_by_date() to find item to be edited"

        # add wait to handle intermittent 'unable to locate element' error esp on Edit scenario
        WebDriverWait(self.browser, timeout=50).until(
                EC.presence_of_element_located((By.XPATH, self.EDIT_OR_ENTRY_PAGE_LOCATOR)))
        page_title = self.browser.find_elements_by_xpath(self.EDIT_OR_ENTRY_PAGE_LOCATOR)
        if not page_title:
            raise RuntimeError(message)

    #endregion

    def wait_for_new_window(self, timeout=10):
        handles_before = self.browser.window_handles
        yield
        WebDriverWait(self.browser, timeout).until(
            lambda driver: len(handles_before) != len(driver.window_handles))
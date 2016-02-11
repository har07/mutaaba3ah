from selenium.common.exceptions import NoSuchElementException
import unittest


class FunctionalTestBase(unittest.TestCase):
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

    #region data manipulation

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

    def delete_item_by_date(self, date):
        # get data sesuai tanggal
        # delete data

        self.validate_browser_property()
        self.validate_at_report_page()

        report_items = self.find_report_items_by_date(date)
        if report_items:
            report_item = report_items[0]

            # click delete
            report_item.click()
            btn_delete = self.browser.find_element_by_id("delete")
            btn_delete.click()

            # pindah ke window konfirmasi & klik delete
            self.browser.switch_to.window(self.browser.window_handles[1])
            submit_delete = self.browser.find_element_by_css_selector("input[type='submit']")
            submit_delete.click()

            # close window konfirmasi & kembai ke halaman sebelumnya
            self.browser.close()
            self.browser.switch_to.window(self.browser.window_handles[0])

    def find_report_items_by_date(self, report_date=""):
        # buka halaman report
        # search data sesuai tanggal
        # format report_date : yyyy-mm-dd

        menu_report = self.browser.find_element_by_id("menu-report")
        menu_mutaaba3ah = self.browser.find_element_by_id("menu-mutaaba3ah")
        menu_mutaaba3ah.click()
        menu_report.click()
        if report_date:
            date_from = self.browser.find_element_by_id("date_from")
            date_from.click()
            date_from.send_keys(report_date)
            date_to = self.browser.find_element_by_id("date_to")
            date_to.click()
            date_to.send_keys(report_date)
        btn_filter = self.browser.find_element_by_id("btn-filter")
        btn_filter.click()
        return self.browser.find_elements_by_css_selector("#mutaaba3ah-table tbody tr")

    #endregion

    #region validation

    def validate_browser_property(self):
        message = "browser property hasn't been initialized: Make sure you have initialized 'self.browser' in setUp()"
        if not self.browser:
            raise RuntimeError(message)

    def validate_at_report_page(self):
        message = "Current page is not Mutaba'ah Report: Make sure you have navigated to Mutaba'ah Report page before calling this method!"
        page_title = self.browser.find_elements_by_xpath("//h2[.=\"Mutaba'ah Report\"]")
        if not page_title:
            raise RuntimeError(message)

    def validate_at_edit_or_entry_page(self):
        # Create a new entry
        message = "Current page is neither Entry nor Edit page: Make sure you have navigated to Create " + \
                  " or Edit Entry page before calling this method!"
        page_title = self.browser.find_elements_by_xpath("//h2[.='Create a new entry' or .='Edit an existing entry']")
        if not page_title:
            raise RuntimeError(message)

    #endregion
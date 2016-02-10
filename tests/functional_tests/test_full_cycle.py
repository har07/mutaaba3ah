from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import datetime

from . import helper


class NewVisitorTest(unittest.TestCase):
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
        helper.logout(self)
        self.browser.quit()

    #region helper methods

    def save_data(self):
        #click button submit on Edit or Entry form

        submit = self.browser.find_element_by_css_selector("input[type='submit']")
        submit.click()

    def input_data(self):
        # populate Entry or Edit form with test data

        dhuha = self.browser.find_element_by_id("id_dhuha")
        dhuha.clear()
        dhuha.send_keys(self.data["dhuha"])
        tilawah_from = self.browser.find_element_by_id("id_tilawah_start")
        tilawah_from.clear()
        tilawah_from.send_keys(self.data["tilawah_from"])
        tilawah_to = self.browser.find_element_by_id("id_tilawah_end")
        tilawah_to.clear()
        tilawah_to.send_keys(self.data["tilawah_to"])
        ql = self.browser.find_element_by_id("id_ql")
        ql.clear()
        ql.send_keys(self.data["ql"])
        shaum = self.browser.find_element_by_xpath("//ul[@id='id_shaum']/li[contains(.,'%s')]" % self.data["shaum"])
        shaum.click()

    def delete_data(self):
        # get data sesuai tanggal
        # delete data

        report_items = self.find_report_items_by_date(self.data["date"])
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

    def assert_data_saved_correctly(self):
        dhuha_display = self.browser.find_element_by_xpath("//table[@id='table-mutaaba3ah-item']/tbody/tr[td='Dhuha']/td[2]")
        self.assertIn(self.data["dhuha"], dhuha_display.text)

        ql_display = self.browser.find_element_by_xpath("//table[@id='table-mutaaba3ah-item']/tbody/tr[td='Qiyamul Lail']/td[2]")
        self.assertIn(self.data["ql"], ql_display.text)

        shaum_display = self.browser.find_element_by_xpath("//table[@id='table-mutaaba3ah-item']/tbody/tr[td='Shaum']/td[2]")
        self.assertIn(self.data["shaum"], shaum_display.text)

        tilawah_display = self.browser.find_element_by_xpath("//table[@id='table-mutaaba3ah-item']/tbody/tr[td='Tilawah']/td[2]")
        self.assertIn(self.data["tilawah_from"], tilawah_display.text)
        self.assertIn(self.data["tilawah_to"], tilawah_display.text)

    #endregion

    def test_login_entrydata_searchreport_logout(self):
        # Brian mendapat informasi dari grup WA ttg aplikasi mutaba'ah harian online
        # Dia mencoba mengakses halaman depan (home) aplikasi tersebut
        self.browser.get("http://localhost:8000")
        helper.try_logout(self) 

        # Brian melihat tidak ada menu apa2 kecuali link untuk login
        self.assertEquals(len(self.browser.find_elements_by_id("user-email")), 0)
        self.assertEquals(len(self.browser.find_elements_by_id("logout")), 0)
        self.assertEquals(len(self.browser.find_elements_by_id("menu-entry")), 0)
        self.assertEquals(len(self.browser.find_elements_by_id("menu-report")), 0)
        helper.login(self)

        # Setelah login, Brian melihat ada menu ke halaman 'Entry' dan 'Report'
        self.assertEquals(len(self.browser.find_elements_by_id("menu-entry")), 1)
        self.assertEquals(len(self.browser.find_elements_by_id("menu-report")), 1)

        # Brian membuka halaman 'Report' untuk memastikan tidak ada data apa2
        # karena ini adalah pertama kalinya ia mengakses aplikasi mutaba'ah ini
        report_items = self.find_report_items_by_date()
        self.assertEquals(len(report_items), 0)

        # Brian kemudian membuka halaman 'Entry',
        # dan mengisikan data mutaba'ah untuk tgl hari ini
        menu_mutaaba3ah = self.browser.find_element_by_id("menu-mutaaba3ah")
        menu_mutaaba3ah.click()
        menu_entry = self.browser.find_element_by_id("menu-entry")
        menu_entry.click()
        self.input_data()
        self.save_data()

        # Setelah disubmit, Brian melihat halaman konfirmasi menunjukkan data
        # sesuai dg yg sudah diisi sebelumnya
        self.assert_data_saved_correctly()
        # error: AssertionError: u"4 raka'at" != '4'

        # Brian beralih ke halaman 'Report' utk memastikan data yg baru saja
        # disubmit, muncul di halaman 'Report'
        report_items = self.find_report_items_by_date(self.data["date"])
        self.assertEquals(len(report_items), 1)
        report_item = report_items[0]

        # Brian menyadari ada inputan yg salah
        # Brian kemudian mengupdate data Dhuha dg angka yang benar
        self.data["dhuha"] = "6"
        report_item.click()
        btn_edit = self.browser.find_element_by_id("edit")
        btn_edit.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.input_data()
        self.save_data()

        # Setelah disubmit, Brian melihat halaman konfirmasi menunjukkan data
        # sesuai update terakhir
        # kemudian Brian menutup halaman konfirmasi tsb
        self.assert_data_saved_correctly()
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])








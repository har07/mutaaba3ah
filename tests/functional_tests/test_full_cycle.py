from selenium import webdriver
import datetime

from . import helper


class NewVisitorTest(helper.FunctionalTestBase):
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
        self.delete_item_by_date(self.data["date"])
        self.logout()
        self.browser.quit()

    #region helper methods

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
        self.try_logout() 

        # Brian melihat tidak ada menu apa2 kecuali link untuk login
        self.assertEquals(len(self.browser.find_elements_by_id("user-email")), 0)
        self.assertEquals(len(self.browser.find_elements_by_id("logout")), 0)
        self.assertEquals(len(self.browser.find_elements_by_id("menu-entry")), 0)
        self.assertEquals(len(self.browser.find_elements_by_id("menu-report")), 0)
        self.login()

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
        self.create_or_edit_data(self.data)

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
        self.create_or_edit_data(self.data)

        # Setelah disubmit, Brian melihat halaman konfirmasi menunjukkan data
        # sesuai update terakhir
        # kemudian Brian menutup halaman konfirmasi tsb
        self.assert_data_saved_correctly()
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])








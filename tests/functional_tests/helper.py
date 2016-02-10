from selenium.common.exceptions import NoSuchElementException

def try_logout(self):
    try:
        logout(self)
    except NoSuchElementException:
        pass

def login(self):
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
    user_email = self.browser.find_element_by_id("user-email")
    user_email.click()
    logout = self.browser.find_element_by_id("logout")
    self.assertIsNotNone(logout)
    logout.click()
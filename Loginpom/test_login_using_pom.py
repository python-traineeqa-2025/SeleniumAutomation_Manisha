import logging
import time

from Setup.Basetest import BaseTest
from PageObjects.loginpage import LoginPage

class TestLogs(BaseTest): # Inherit from BaseTest

    def __init__(self, driver):
        self.driver = driver

    def test_first(self):
        url = self.creds["base_url"]
        self.driver.get( url)  # Ensure correct URL format
        logging.info("Opened the site")
        login_page = LoginPage(self.driver)
        uname = self.creds["standard_username"]
        pwd = self.creds["Password_for_all_users"]
        login_page.login(uname,pwd)
        login_page.login(uname,pwd)
        time.sleep(5)
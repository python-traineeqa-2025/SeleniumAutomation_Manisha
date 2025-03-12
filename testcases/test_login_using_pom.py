
import logging
import time

from Setup.Basetest import BaseTest

from Page_objects.loginpom.loginpage import LoginPage
class TestLogs(BaseTest):

    # def __init__(self, creds,driver):
    #     self.creds = creds
    #     self.driver = driver

    def test_login(self):
        url = self.creds["base_url"]
        self.driver.get( url)
        logging.info("Opened the site")

        login_page = LoginPage(self.driver)
        logging.info("getting the credentials")

        uname = self.creds["standard_username"]
        password = self.creds["Password_for_all_users"]
        logging.info("got the credentials now logging in")
        login_page.login(uname,password)
        logging.info("logged in")

        time.sleep(5)
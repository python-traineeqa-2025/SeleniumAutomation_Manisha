import logging
import time

from Setup.Basetest import BaseTest
from selenium.webdriver.common.by import By


class Testlog(BaseTest):

    def test_first(self):
        url = self.creds["base_url"]
        self.driver.get(url)
        logging.info("OPEN SAUCE.COM")
        title = self.driver.title
        logging.info("SITE OPENED:")

        username_input = self.driver.find_element(By.ID, 'user-name')
        username_input.click()
        username_input.send_keys('standard_user')
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.click()
        password_input.send_keys('secret_sauce')
        submit_btn = self.driver.find_element(By.ID, 'login-button')
        submit_btn.click()
        time.sleep(5)

    # def test_first1(self):
    #     url = self.creds["base_url"]
    #     self.driver.get(url)
    #     logging.info("OPEN SAUCE.COM")
    #     title = self.driver.title
    #     logging.info("SITE OPENED:")
    #     list_cred = self.creds['users']
    #
    #     # log_cred_list = []
    #
    #     for i in list_cred:
    #
    #
    #         username_input = self.driver.find_element(By.ID, 'user-name')
    #         username_input.click()
    #         uname = self.creds(list_cred.keys())
    #         username_input.send_keys(uname)
    #         password_input = self.driver.find_element(By.ID, 'password')
    #         password_input.click()
    #         password_input.send_keys(self.creds(list_cred.value()))
    #         submit_btn = self.driver.find_element(By.ID, 'login-button')
    #         submit_btn.click()
    #         time.sleep(5)



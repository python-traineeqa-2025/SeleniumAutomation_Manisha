import logging
import time

from Setup.Basetest import BaseTest
from selenium.webdriver.common.by import By


class Testlog(BaseTest):

    def test_login(self):

        url = self.creds['base_url']
        self.driver.get(url)
        logging.info("OPEN SITE:")
        title = self.driver.title
        logging.info("Site Opened:")
        log_cred = self.creds['users']

        # for i in log_cred:

        username = self.driver.find_element(By.ID,'user-name')
        username.click()
        user_name = self.creds['problem_user']
        username.send_keys(user_name)
        password = self.driver.find_element(By.ID,'password')
        password.click()
        password.send_keys(self.creds['Password_for_all_users'])
        submit_button = self.driver.find_element(By.ID,'login-button')
        submit_button.click()
        time.sleep(5)

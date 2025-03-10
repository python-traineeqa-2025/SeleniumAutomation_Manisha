#Assignment
import logging
import time

from Setup.Basetest import BaseTest

from selenium.webdriver.common.by import By


class Test_Multiple_logs(BaseTest):

    def test_login(self):
        url = self.creds["base_url"]
        self.driver.get(url)
        logging.info("OPEN SAUCE.COM")
        title = self.driver.title
        logging.info("SITE OPENED:")

        list_creds = self.creds['users']

        for username, password in list_creds.items():
            #items dict ko key ra value pull garcha

            user_name = self.driver.find_element(By.ID,'user-name')
            user_name.clear()
            user_name.send_keys(username)
            print(user_name)

            pwd = self.driver.find_element(By.ID,'password')
            pwd.clear()
            pwd.send_keys(password)

            submit_btn = self.driver.find_element(By.ID,'login-button')
            submit_btn.click()
            time.sleep(5)


            self.driver.back()

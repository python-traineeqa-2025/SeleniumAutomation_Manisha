import json
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BaseTest:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)

    def setup_method(self, method):
        # driver_path = r"C:\Users\manishag\OneDrive - Infinite Computer Solutions (India) Limited\Documents\AutomationWithSelenium\Bin\chromedriver.exe"
        #
        # ser = Service(driver_path)
        # logging.info("set up driver")
        # driver = webdriver.Chrome(service=ser)
        self.driver = webdriver.Chrome()
        # self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        creds_path = r"C:\Users\manishag\OneDrive - Infinite Computer Solutions (India) Limited\Documents\AutomationWithSelenium\Credentials\creds.json"
        with open(creds_path, "r") as f:
            self.creds = json.load(f)

    def teardown_method(self, method):
        self.driver.quit()
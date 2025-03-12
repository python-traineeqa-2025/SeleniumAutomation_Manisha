import json
import logging

from selenium import  webdriver
from selenium.webdriver.chrome.service import Service


class BaseTest:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)

    # def __init__(self,driver):
    #     self.driver = driver

    def setup_method(self,method):

        self.driver = webdriver.Chrome()

        # driver_path = r"C:\Users\manishag\OneDrive - Infinite Computer Solutions (India) Limited\Documents\Final Project\Bin\chromedriver.exe"
        #
        # ser = Service(driver_path)
        #
        # logging.info("set up driver")
        #
        # driver = webdriver.Chrome(service=ser)
        #
        # self.driver = driver

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        creds_path = r"C:\Users\manishag\OneDrive - Infinite Computer Solutions (India) Limited\Documents\AutomationWithSelenium\Credentials\credsbhojdeals.json"
        with open(creds_path,'r') as f:
            self.credsbhojdeals = json.load(f)

    # def teardown_method(self,method):
    #     self.driver.quit()
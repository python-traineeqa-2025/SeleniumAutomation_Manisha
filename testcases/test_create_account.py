
import logging
import time

# from Setup.Basetest import BaseTest
from Setup.BhojBasetest import BaseTest
from Page_objects.Bhojdeals.createaccount import CreateAccount

class TestLogs(BaseTest):

    # def __init__(self, creds,driver):
    #     self.creds = creds
    #     self.driver = driver

    def test_create(self):
        url = self.credsbhojdeals["Base_url"]
        self.driver.get( url)
        logging.info("Opened the site")

        create_page = CreateAccount(self.driver)
        logging.info("getting the credentials")

        fname = self.credsbhojdeals["Name"]
        # lname = self.creds["lastname"]
        email = self.credsbhojdeals["email_address"]
        password = self.credsbhojdeals["password"]
        confirm_password = self.credsbhojdeals["Confirm_Password"]
        mobile = self.credsbhojdeals["Mobile-Number"]
        logging.info("got the credentials now logging in")
        create_page.create(fname,email,password,confirm_password,mobile)
        logging.info("Account Created Successfully")

        time.sleep(10)
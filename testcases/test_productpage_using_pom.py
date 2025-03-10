import logging
import time

from Setup.Basetest import BaseTest
from Page_objects.loginpom.loginpage import LoginPage
from Page_objects.Productpagepom.productpage import Productpage

class TestProduct(BaseTest):

    def test_product(self):
        url = self.creds["base_url"]
        self.driver.get(url)
        logging.info("Opened the site")

        login_page = LoginPage(self.driver)
        logging.info("getting the credentials")

        uname = self.creds["standard_username"]
        password = self.creds["Password_for_all_users"]
        logging.info("got the credentials now logging in")
        login_page.login(uname, password)

        des = Productpage(self.driver)
        # des.product()
        logging.info("Clicked on the product title and navigated to the product detail page")
        des.product()
        # logging.info(product_des)
        time.sleep(2)

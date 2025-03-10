import logging
import time

from Page_objects.loginpom.loginpage import LoginPage
from Page_objects.Cartpage.Cartpage import CartPage
from Setup.Basetest import BaseTest

class TestCartButton(BaseTest):

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

        Cart_P = CartPage(self.driver)
        Cart_P.cart()

        time.sleep(2)

        logging.info("Products successfully added to the cart")

        # Check if the product is in the cart
        product_name = "Sauce Labs Bolt T-Shirt"
        if Cart_P.is_product_in_cart(product_name):
            logging.info(f"Product '{product_name}' is in the cart.")
        else:
            logging.info(f"Product '{product_name}' is not in the cart.")
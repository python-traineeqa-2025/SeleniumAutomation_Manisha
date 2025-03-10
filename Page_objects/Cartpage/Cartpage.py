import time

from Page_objects.Cartpage.cartpageproperties import CartPageProperties
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage(CartPageProperties):

    def __init__(self,driver):
        self.driver = driver


    def cart(self):

        cart_btn = self.Cart_Button()
        cart_btn.click()

        cart_btn1 = self.Cart_button1()
        cart_btn1.click()

        CartIcon = self.Cart_Icon()
        CartIcon.click()
        time.sleep(5)

    def is_product_in_cart(self, product_name):
        try:
            # Wait for the cart items to be visible
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{product_name}")]'))
            )
            product = self.driver.find_element(By.XPATH, f'//div[contains(text(), "{product_name}")]')
            return True
        except:
            return False
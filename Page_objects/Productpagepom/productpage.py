import logging

from Page_objects.Productpagepom.productpageproperties import Product_Page_Properties

class Productpage(Product_Page_Properties):

    def __init__(self, driver):
        self.driver = driver

    def product(self):
        product = self.product_click
        product.click()

        description= self.description_print()
        description1 = description.text
        logging.info(description1)

        price= self.price_print()
        price1 = price.text
        logging.info(price1)


        # Assuming description_element has a text attribute or method to get the description
        # return description_element.text
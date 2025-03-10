from Page_objects.Productpagepom.Productpagelocators import Product_Page_Locators

class Product_Page_Properties(Product_Page_Locators):

    @property

    def product_click(self):
        return self.driver.find_element(*Product_Page_Locators.Product)

    def description_print(self):
        return self.driver.find_element(*Product_Page_Locators.Description)

    def price_print(self):
        return self.driver.find_element(*Product_Page_Locators.Price)

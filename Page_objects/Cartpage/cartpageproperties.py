from Page_objects.Cartpage.cartpagelocators import CartPage_Locators

class CartPageProperties(CartPage_Locators):

    def Cart_Button(self):
        return self.driver.find_element(*CartPage_Locators.Cart_Button)

    def Cart_button1(self):
        return  self.driver.find_element(*CartPage_Locators.Cart_Button1)

    def Cart_Icon(self):
        return self.driver.find_element(*CartPage_Locators.Cart_Icon)

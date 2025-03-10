from Page_objects.loginpom.loginpagelocators import Login_page_locators


class LoginPageProperties(Login_page_locators):

    @property
    def user_name_input(self):
        return self.driver.find_element(*Login_page_locators.USERNAME)

    @property
    def password_input(self):
        return self.driver.find_element(*Login_page_locators.PASSWORD)

    @property
    def submit_button_click(self):
        return self.driver.find_element(*Login_page_locators.SUBMIT_BUTTON)

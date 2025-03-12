
from Page_objects.Bhojdeals.Createaccountlocators import CreateAccountLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Create_Account_Properties(CreateAccountLocators):


    @property
    def signup_btn(self):
        return self.driver.find_element(*CreateAccountLocators.SIGN_UP)
    @property
    def Name_input(self):
        return self.driver.find_element(*CreateAccountLocators.NAME)

    # @property
    # def lastname_input(self):
    #     return self.driver.find_element(*CreateAccountLocators.)

    @property
    def email_input(self):
        return self.driver.find_element(*CreateAccountLocators.EMAIL_ADDRESS)

    @property

    def password_input(self):
        return self.driver.find_element(*CreateAccountLocators.PASSWORD)

    @property

    def confirmpassword_input(self):
        return self.driver.find_element(*CreateAccountLocators.CONFORM_PASSWORD)


    # @property
    # def submit_btn(self):
    #     return WebDriverWait(self.driver, 50).until(
    #         EC.element_to_be_clickable(CreateAccountLocators.SUBMIT_BUTTON)
    #     )
    @property
    def country_dropdown(self):
        return self.driver.find_element(*CreateAccountLocators.COUNTRY)

    @property
    def mobile_input(self):
        return self.driver.find_element(*CreateAccountLocators.MOBILE_NUMBER)
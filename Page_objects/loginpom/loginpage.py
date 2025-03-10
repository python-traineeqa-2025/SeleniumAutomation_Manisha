# import self
from Page_objects.loginpom.loginpageproperties import LoginPageProperties

class LoginPage(LoginPageProperties):

    def __init__(self, driver):
        self.driver = driver


    def login(self, username, password):

        uname = self.user_name_input
        uname.click()
        uname.send_keys(username)

        pwd = self.password_input
        pwd.click()
        pwd.send_keys(password)

        submit_button = self.submit_button_click
        submit_button.click()

import time

from select import select
from selenium.webdriver.support.select import Select

from Page_objects.Bhojdeals.CreateAccountProperties import Create_Account_Properties

class CreateAccount(Create_Account_Properties):

    def __init__(self,driver):
        self.driver = driver


    def create(self,Name,email,password,confirmpassword,mobile_num):

        signup = self.signup_btn
        signup.click()

        fn = self.Name_input
        fn.send_keys(Name)

        # ln = self.lastname_input
        # ln.send_keys(lastname)

        email_p = self.email_input
        email_p.send_keys(email)

        pwd = self.password_input
        pwd.send_keys(password)

        c_pwd = self.confirmpassword_input
        c_pwd.send_keys(confirmpassword)

        # create_btn = self.submit_btn
        # self.driver.execute_script("arguments[0].scrollIntoView();", create_btn)
        # create_btn.click()
        country_element = self.country_dropdown
        drp = Select(country_element)
        drp.select_by_visible_text("Nepal")

        country_element = self.country_dropdown
        drp = Select(country_element)
        drp.select_by_index(5)



        mobile = self.mobile_input
        mobile.send_keys(mobile_num)
        time.sleep(10)









    # def create(self,first_name,last_name,email,pwd,confirm_pwd):
    #
    #     sign_in = self.signin_btn
    #     sign_in.click()
    #
    #     fn= self.firstname_input
    #     # fname.click()
    #     fn.send_keys(first_name)
    #
    #     ln = self.lastname_input
    #     # lname.click()
    #     ln.send_keys(last_name)
    #
    #     email1 = self.email_input
    #     # email_address.click()
    #     email1.send_keys(email)
    #
    #     pass_word = self.password_input
    #     # pass_word.click()
    #     pass_word.send_keys(pwd)
    #
    #     confirm = self.confirmpassword_input
    #     # confirm.click()
    #     confirm.send_keys(confirm_pwd)
    #
    #     submit = self.submit_btn
    #     submit.click()




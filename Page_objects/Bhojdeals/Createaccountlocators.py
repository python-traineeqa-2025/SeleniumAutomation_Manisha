from selenium.webdriver.common.by import By

class CreateAccountLocators(object):

    SIGN_UP = (By.XPATH,'//*[@id="nav_collapse"]/ul/ul/li[2]')
    NAME = (By.ID,'inlinefromusername')
    # LASTNAME = (By.ID,'lastname')
    EMAIL_ADDRESS = (By.ID, "inlinefromemail")
    PASSWORD = (By.ID,'inlinefrompassword')
    CONFORM_PASSWORD = (By.ID,'inlinefromconfpassword')
    COUNTRY = (By.ID,'__BVID__84')
    MOBILE_NUMBER = (By.ID,'inlineFormInputGroup')
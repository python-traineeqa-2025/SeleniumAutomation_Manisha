from selenium.webdriver.common.by import By

class Product_Page_Locators(object):

    Product = (By.XPATH,'//*[@id="item_4_title_link"]/div')

    Description = (By.XPATH, "//div[@class='inventory_details_desc large_size']")

    Price = (By.XPATH,"//div[@class='inventory_details_price']")
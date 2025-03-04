import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.page import navigate
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



driver_path = r"C:\Users\manishag\OneDrive - Infinite Computer Solutions (India) Limited\Documents\AutomationWithSelenium\Bin\chromedriver.exe"

service1 = Service(driver_path)

driver = webdriver.Chrome(service = service1)

base_url = "https://www.saucedemo.com"
driver.get(base_url)


print("PRINTING THE DETAILS OF THE PRODUCT:\n")
username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("standard_user")
password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
login = driver.find_element(By.ID,"login-button")
login.click()
time.sleep(2)
product1 = driver.find_element(By.ID,'item_4_img_link')
product1.click()
description = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[2]'))
)
print(description.text)

price = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="inventory_item_container"]/div/div/div[2]/div[3]'))
)
print(price.text)



driver.get(base_url)
username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("standard_user")
password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
login = driver.find_element(By.ID,"login-button")
login.click()
time.sleep(2)
product1 = driver.find_element(By.ID,'item_4_img_link')
product1.click()
nav_back = driver.find_element(By.ID,'back-to-products')
nav_back.click()
assert driver.current_url == "https://www.saucedemo.com/inventory.html"

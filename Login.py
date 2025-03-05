import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#here r is raw text

driver_path = r"C:\Users\manishag\OneDrive - Infinite Computer Solutions (India) Limited\Documents\AutomationWithSelenium\Bin\chromedriver.exe"

service1 = Service(driver_path)

driver = webdriver.Chrome(service = service1)
driver.get("https://www.saucedemo.com")

username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("standard_user")
time.sleep(3)
password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
login = driver.find_element(By.ID,"login-button")
login.click()
assert "Swag Labs" in driver.title
print(driver.title)

print("Invalid Login")
driver.get("https://www.saucedemo.com")
username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("standard_user")
time.sleep(1)
password = driver.find_element(By.ID,"password")
password.send_keys("secret_saucee")
login = driver.find_element(By.ID,"login-button")
login.click()
time.sleep(5)
error_message = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3"))
)
assert "Epic sadface: Username and password do not match any user in this service" in error_message.text
print(error_message.text)



print("Empty Password Field")
driver.get("https://www.saucedemo.com")
username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("standard_user")
time.sleep(1)
password = driver.find_element(By.ID,"password")
password.send_keys("")
login = driver.find_element(By.ID,"login-button")
login.click()
time.sleep(5)
error_message = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3"))
    )
assert "Epic sadface: Password is require" in error_message.text
print(error_message.text)


print("Empty Username Field")
driver.get("https://www.saucedemo.com")
username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("")
time.sleep(1)
password = driver.find_element(By.ID,"password")
password.send_keys("Secret Sauce")
login = driver.find_element(By.ID,"login-button")
login.click()
time.sleep(2)
error_message = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
assert "Epic sadface: Username is require" in error_message.text
print(error_message.text)


print("Empty Username and Password Field")
driver.get("https://www.saucedemo.com")
username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("")
time.sleep(1)
password = driver.find_element(By.ID,"password")
password.send_keys("")
login = driver.find_element(By.ID,"login-button")
login.click()
time.sleep(2)
error_message = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
assert "Epic sadface: Username is require" in error_message.text
print(error_message.text)

print("Invalid Username")
driver.get("https://www.saucedemo.com")
username = driver.find_element(By.ID,"user-name")
username.click()
username.send_keys("fasgdasfd")
time.sleep(1)
password = driver.find_element(By.ID,"password")
password.send_keys("secret_sauce")
login = driver.find_element(By.ID,"login-button")
login.click()
time.sleep(2)
error_message = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
assert "Epic sadface: Username and password do not match any user in this service" in error_message.text
print(error_message.text)



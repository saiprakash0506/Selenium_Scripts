from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.maximize_window()


driver.get("https://www.saucedemo.com")


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)


buttons = driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
for i in range(2):
    buttons[i].click()
time.sleep(2)


driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)


driver.find_element(By.ID, "checkout").click()
time.sleep(2)

driver.find_element(By.ID, "first-name").send_keys("Sai")
driver.find_element(By.ID, "last-name").send_keys("Reddy")
driver.find_element(By.ID, "postal-code").send_keys("500001")
driver.find_element(By.ID, "continue").click()
time.sleep(2)


driver.find_element(By.ID, "finish").click()
driver.save_screenshot("Order_finished.png")
time.sleep(2)

print("Order Placed Successfully")

time.sleep(1)
driver.quit()

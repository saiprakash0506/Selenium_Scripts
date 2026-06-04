from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)

#step 1
driver.get("https://www.amazon.in")
time.sleep(3)

#step2
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Laptops")
search_box.send_keys(Keys.ENTER)

time.sleep(2)

driver.execute_script("window.scrollBy(0, 500);")
time.sleep(2)

#step3
print("Page Title:", driver.title)

#step4
print("Current URL:", driver.current_url)

#step5
driver.save_screenshot("amazon_laptops.png")

print("\nScreenshot Captured Successfully")

driver.quit()

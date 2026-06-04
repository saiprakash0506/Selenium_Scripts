from selenium import webdriver
from selenium.webdriver.common.by import By
import csv, time

driver = webdriver.Chrome()

driver.maximize_window()

#step 1
driver.get("https://www.flipkart.com/search?q=mobiles&sort=price_desc")
time.sleep(4)

#step2
try:
    driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()
except:
    pass
time.sleep(2)

data = []
#step3
cards = driver.find_elements(By.XPATH, "//div[@data-id]")

for card in cards:
    name = card.find_element(By.CLASS_NAME, "RG5Slk").text.strip()
    price = card.find_element(By.CLASS_NAME, "hZ3P6w").text.strip()
    if name and price:
        data.append([name, price])
    if len(data) >= 5:
        break

#step4

with open("flipkart_products.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Product Name", "Price"])
    w.writerows(data)

#step5 

print(f"✅ Saved {len(data)} products to flipkart_products.csv")
driver.quit()

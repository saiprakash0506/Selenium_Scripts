from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

phonenumber = "9910265271"
card_numberr = "6061003829100210"
expirydate = "0329"
cvv = "575"

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)
time.sleep(2)
driver.get("https://www.airtel.in")
search_box = driver.find_element(By.ID, "rechargeInput")
search_box.send_keys(phonenumber)

time.sleep(5)

print(driver.current_url)

Truly_unlimited = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "tabsHeaderButton-10"))
)

driver.execute_script("arguments[0].click();", Truly_unlimited)
time.sleep(5)
card = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/div[11]/div/div[2]/div[2]/div/div[1]/div[2]",
)

card.click()

time.sleep(5)

driver.execute_script("window.scrollBy(0, 500);")
creditcard = driver.find_element(By.ID, "accordion-header-2")
creditcard.click()

time.sleep(3)
WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.ID, "cardNumber"))
).send_keys(card_numberr)
time.sleep(3)
expiry = driver.find_element(By.ID, "cardExpiry").send_keys(expirydate)
time.sleep(3)
driver.find_element(By.ID, "cardCvv").send_keys(cvv)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "[data-testid='makePaymentBtn']").click()
time.sleep(20)

Payment_failed = driver.save_screenshot("paymentfailed.png")
driver.quit()

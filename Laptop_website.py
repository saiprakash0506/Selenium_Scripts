from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.get("https://www.apple.com/in")
mac = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-globalnav-item-name='mac']"))
)
driver.execute_script("arguments[0].click();", mac)
time.sleep(3)
driver.execute_script("window.scrollBy(0, 300)")
time.sleep(2)
macbook_pro = driver.find_element(
    By.CSS_SELECTOR, "a[data-analytics-title='macbook pro']"
)
driver.execute_script("arguments[0].click();", macbook_pro)
time.sleep(5)
buy_btn = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Buy, MacBook Pro']")
buy_btn.click()
time.sleep(5)
size_14 = driver.find_element(
    By.CSS_SELECTOR, "input[data-autom='chassis-dimensionScreensize14inch']"
)
driver.execute_script("arguments[0].click();", size_14)
time.sleep(2)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(2)
space_black = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[data-autom='chassis-dimensionColorspaceblack']")
    )
)
driver.execute_script("arguments[0].click();", space_black)
driver.execute_script("window.scrollBy(0, 400)")
time.sleep(2)
standard_display = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[data-autom='display-dimensionFinishstandard']")
    )
)
driver.execute_script("arguments[0].click();", standard_display)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(2)
m5_chip = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[data-autom='processor-dimensionChipm5']")
    )
)
driver.execute_script("arguments[0].click();", m5_chip)
driver.execute_script("window.scrollBy(0, 600)")
time.sleep(2)
final_cut_no = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (
            By.CSS_SELECTOR,
            "input[data-autom='software_final-preInstalledSoftwarenone']"
        )
    )
)
driver.execute_script("arguments[0].click();", final_cut_no)
logic_no = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (
            By.CSS_SELECTOR,
            "input[data-autom='software_logic-preInstalledSoftwarenone']"
        )
    )
)
driver.execute_script("arguments[0].scrollIntoView({block:'center'});",logic_no
)
time.sleep(2)
driver.execute_script("arguments[0].click();",logic_no)
driver.execute_script("window.scrollBy(0, 500)")
time.sleep(2)
applecare_no = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (
            By.CSS_SELECTOR,
            "input[data-autom='noapplecare']"
        )
    )
)
driver.execute_script("arguments[0].click();", applecare_no)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)
add_to_bag = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (
            By.CSS_SELECTOR,
            "button[data-autom='add-to-cart']"
        )
    )
)
driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    add_to_bag
)
time.sleep(2)
driver.save_screenshot("apple_bag.png")
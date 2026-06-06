from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyperclip
import time

TOPIC = "Ayar Sheer"

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://www.youtube.com")
    time.sleep(3)

    # Search
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
    search_box.send_keys(TOPIC)
    search_box.send_keys(Keys.ENTER)

    time.sleep(5)

    # Open Filters
    filter_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@aria-label,'Search filters')]")
        )
    )
    filter_button.click()

    time.sleep(2)

    # This year
    try:
        this_year = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//yt-formatted-string[normalize-space()='This year']/ancestor::a[@id='endpoint']",
                )
            )
        )
        driver.execute_script("arguments[0].click();", this_year)
        print("Applied: This year")
        time.sleep(4)
    except:
        print("This year filter not found")

    # Popularity
    try:
        filter_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@aria-label,'Search filters')]")
            )
        )
        filter_button.click()

        time.sleep(2)

        popularity = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//yt-formatted-string[normalize-space()='Popularity']/ancestor::a[@id='endpoint']",
                )
            )
        )

        driver.execute_script("arguments[0].click();", popularity)
        print("Applied: Popularity")
        time.sleep(5)

    except:
        print("Popularity filter not found")

    # Open first result
    first_video = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//a[@id='video-title'])[1]"))
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", first_video
    )

    time.sleep(2)
    first_video.click()

    time.sleep(3)

    # Copy URL
    video_url = driver.current_url
    pyperclip.copy(video_url)

    print("\nVideo URL:")
    print(video_url)
    print("\nURL copied to clipboard!")

    # Pause video
    try:
        driver.execute_script("""
        let video = document.querySelector('video');
        if(video){
            video.pause();
        }
    """)
        print("Video paused")
    except Exception as e:
        print("Could not pause video:", e)
    # Open new tab
    driver.switch_to.new_window("tab")

    # Navigate to website
    driver.get("https://highreach.ai/tools/youtube-video-downloader")

    # Wait for page to load
    time.sleep(2)

    # Find the first input field and paste URL
    url_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input")))

    url_box.clear()
    url_box.send_keys(video_url)

    print("URL pasted into input field")
    time.sleep(2)

    button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Download YouTube Video']")
        )
    )

    # Move to the button and simulate a real, physical mouse click sequence
    print("Performing hardware-level click sequence...")
    actions = ActionChains(driver)
    actions.move_to_element(button).click().perform()
    print("Click sequence sent successfully.")
    time.sleep(5)
    print("Waiting 10 seconds for media options to appear...")

    # 4. Scroll down to the newly loaded video section
    print("Scrolling down to the media results...")
    # Finding the text text label "Media found" to anchor our scroll position
    media_section = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Media found')]")
        )
    )
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
        media_section,
    )
    time.sleep(1)  # Short pause for the scroll smooth effect to finish

    # 6. Target and click the first resolution download link (<a> tag)
    print("Targeting the first resolution link...")

    # This targets the very first <a> tag inside the media container that has a download attribute
    first_link_xpath = "(//a[@download and contains(@class, 'flex')])[1]"

    first_download_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, first_link_xpath))
    )

    # Since it's a direct download hyperlink, a standard click or JS click works perfectly here
    driver.execute_script("arguments[0].click();", first_download_link)
    print("Success: Clicked the resolution download link!")
    time.sleep(30)
finally:
    driver.quit()

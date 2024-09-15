from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(service=Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe"))

try:
    driver.get("https://www.amazon.com")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)


    drop_down = wait.until(EC.presence_of_element_located((By.ID, "searchDropdownBox")))
    drop_down.send_keys("Software")

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("games")
    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()

    time.sleep(5)

finally:
    driver.quit()
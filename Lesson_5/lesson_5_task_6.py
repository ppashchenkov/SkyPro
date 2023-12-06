from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

open_url = "http://the-internet.herokuapp.com/entry_ad"
blue_button = ".btn-primary"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(open_url)

WebDriverWait(driver, 2000).until(EC.

sleep(2)

# driver.find_element(By.XPATH, "//*[@id='modal]/div[2]/div[3]/p").click()

sleep(3)

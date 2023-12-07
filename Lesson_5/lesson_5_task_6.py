from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

open_url = "http://the-internet.herokuapp.com/entry_ad"
close_button_xpath = "//*[@id='modal']/div[2]/div[3]/p"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(open_url)

try:
    close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, close_button_xpath)))
    close.click()
except:
    driver.quit()

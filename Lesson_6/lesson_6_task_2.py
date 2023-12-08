from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

open_url = "http://uitestingplayground.com/textinput"
text_field = "input[placeholder='MyButton']"
blue_button = "button#updatingButton"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get(open_url)
driver.find_element(By.CSS_SELECTOR, text_field).send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, blue_button).click()

print(driver.find_element(By.CSS_SELECTOR, blue_button).text)

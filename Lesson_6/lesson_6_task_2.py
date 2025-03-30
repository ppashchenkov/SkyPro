from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

open_url = "http://uitestingplayground.com/textinput"
text_field = "input[placeholder='MyButton']"
blue_button = "button#updatingButton"

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.maximize_window()

driver.get(open_url)
driver.find_element(By.CSS_SELECTOR, text_field).send_keys("Sky_Pro")
driver.find_element(By.CSS_SELECTOR, blue_button).click()
sleep(5)
print(driver.find_element(By.CSS_SELECTOR, blue_button).text)
driver.quit()
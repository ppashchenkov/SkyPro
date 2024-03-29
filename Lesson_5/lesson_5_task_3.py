from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

open_url = "http://the-internet.herokuapp.com/add_remove_elements/"
add_element = "button[onclick='addElement()']"
delete_list = "button[onclick='deleteElement()']"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#
# for browser in browsers:
#     driver = browser
#
driver.maximize_window()
driver.get(open_url)
for i in range(0,5):
    driver.find_element(By.CSS_SELECTOR,add_element).click()
print(f"Количество кнопок Delete = {len(driver.find_elements(By.CSS_SELECTOR, delete_list))}")
driver.quit()

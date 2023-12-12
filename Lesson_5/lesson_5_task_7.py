from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

open_url = "http://the-internet.herokuapp.com/inputs"
input_number_locator = "input[type='number']"

browsers = [webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
            webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            ]

for browser in browsers:
    driver = browser
    driver.maximize_window()
    driver.get(open_url)

    driver.find_element(By.CSS_SELECTOR, input_number_locator).send_keys("1000")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, input_number_locator).clear()
    driver.find_element(By.CSS_SELECTOR, input_number_locator).send_keys("999")
    sleep(2)
    driver.quit()

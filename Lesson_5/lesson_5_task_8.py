from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

open_url = "http://the-internet.herokuapp.com/login"
username = "tomsmith"
password = "SuperSecretPassword!"
username_locator = "input[name='username']"
password_locator = "input[name='password']"
login_button = "button[type='submit']"

browsers = [webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
            webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            ]

for browser in browsers:
    driver = browser
    driver.maximize_window()
    driver.get(open_url)

    driver.find_element(By.CSS_SELECTOR, username_locator).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, password_locator).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, login_button).click()
    sleep(5)
    driver.quit()

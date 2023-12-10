from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def calculator(delay_):
    open_url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    delay_locator = "input#delay"
    button_7_locator = "//*[@id='calculator']/div[2]/span[1]"
    button_plus_locator = "//*[@id='calculator']/div[2]/span[4]"
    button_8_locator = "//*[@id='calculator']/div[2]/span[2]"
    button_itis_locator = "//*[@id='calculator']/div[2]/span[15]"
    result_locator = "div.screen"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(open_url)
    driver.find_element(By.CSS_SELECTOR, delay_locator).clear()
    driver.find_element(By.CSS_SELECTOR, delay_locator).send_keys(45)
    driver.find_element(By.XPATH, button_7_locator).click()
    driver.find_element(By.XPATH, button_plus_locator).click()
    driver.find_element(By.XPATH, button_8_locator).click()
    driver.find_element(By.XPATH, button_itis_locator).click()

    print("R = " + driver.find_element(By.CSS_SELECTOR, result_locator).text)
    sleep(delay_)
    print("R = " + driver.find_element(By.CSS_SELECTOR, result_locator).text)

    return driver.find_element(By.CSS_SELECTOR, result_locator).text

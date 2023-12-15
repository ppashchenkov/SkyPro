from selenium.webdriver.common.by import By
from time import sleep


class MainPage:
    open_url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    delay_locator = "input#delay"
    button_7_locator = "//*[@id='calculator']/div[2]/span[1]"
    button_plus_locator = "//*[@id='calculator']/div[2]/span[4]"
    button_8_locator = "//*[@id='calculator']/div[2]/span[2]"
    button_itis_locator = "//*[@id='calculator']/div[2]/span[15]"
    result_locator = "div.screen"

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.open_url)

    def set_delay(self):
        self._driver.find_element(By.CSS_SELECTOR, self.delay_locator).clear()
        self._driver.find_element(By.CSS_SELECTOR, self.delay_locator).send_keys(45)

    def get_7_plus_8(self):
        self._driver.find_element(By.XPATH, self.button_7_locator).click()
        self._driver.find_element(By.XPATH, self.button_plus_locator).click()
        self._driver.find_element(By.XPATH, self.button_8_locator).click()
        self._driver.find_element(By.XPATH, self.button_itis_locator).click()

    def get_result(self, _delay):
        sleep(_delay)
        return self._driver.find_element(By.CSS_SELECTOR, self.result_locator).text
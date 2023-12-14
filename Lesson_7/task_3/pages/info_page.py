from selenium.webdriver.common.by import By


class InfoPage:
    first_name_locator = "input#first-name"
    last_name_locator = "input#last-name"
    zip_code_locator = "input#postal-code"
    continue_locator = "input#continue"

    def __init__(self, driver):
        self._driver = driver

    def enter_your_details(self):
        self._driver.find_element(By.CSS_SELECTOR, self.first_name_locator).send_keys("Peter")
        self._driver.find_element(By.CSS_SELECTOR, self.last_name_locator).send_keys("Ivanov")
        self._driver.find_element(By.CSS_SELECTOR, self.zip_code_locator).send_keys("100101")
        self._driver.find_element(By.CSS_SELECTOR, self.continue_locator).click()

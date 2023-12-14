from selenium.webdriver.common.by import By


class CartPage:
    checkout_button = "button[name='checkout']"

    def __init__(self, driver):
        self._driver = driver

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, self.checkout_button).click()

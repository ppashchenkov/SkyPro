from selenium.webdriver.common.by import By


class CheckoutPage:
    total_locator = "div.summary_total_label"

    def __init__(self, driver):
        self._driver = driver

    def get_total(self):
        total =  self._driver.find_element(By.CSS_SELECTOR, self.total_locator).text
        return total

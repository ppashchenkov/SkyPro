from selenium.webdriver.common.by import By


class MainPage:
    add_to_cart_sauce_labs_backpack = "button[data-test='add-to-cart-sauce-labs-backpack']"
    add_to_cart_sauce_labs_bolt_t_shirt = "button[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
    add_to_cart_sauce_labs_onesie = "button[data-test='add-to-cart-sauce-labs-onesie']"
    to_shopping_cart = "a.shopping_cart_link"

    def __init__(self, driver):
        self._driver = driver

    def add_items_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, self.add_to_cart_sauce_labs_backpack).click()
        self._driver.find_element(By.CSS_SELECTOR, self.add_to_cart_sauce_labs_bolt_t_shirt).click()
        self._driver.find_element(By.CSS_SELECTOR, self.add_to_cart_sauce_labs_onesie).click()

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, self.to_shopping_cart).click()

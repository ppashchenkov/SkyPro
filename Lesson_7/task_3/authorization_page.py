from selenium.webdriver.common.by import By


class AuthPage:
    open_url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    username_locator = "input#user-name"
    password_locator = "input#password"
    login_button = "input#login-button"

    def __init__(self, _driver):
        self._driver = _driver
        self._driver.maximize_window()
        self._driver.get(self.open_url)

    def authorization(self):
        self._driver.find_element(By.CSS_SELECTOR, self.username_locator).send_keys(self.username)
        self._driver.find_element(By.CSS_SELECTOR, self.password_locator).send_keys(self.password)
        self._driver.find_element(By.CSS_SELECTOR, self.login_button).click()

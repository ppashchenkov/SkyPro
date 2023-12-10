from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def swag_labs_shopping(my_users_):
    open_url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    username_locator = "input#user-name"
    password_locator = "input#password"
    login_button = "input#login-button"
    add_to_cart_sauce_labs_backpack = "button[data-test='add-to-cart-sauce-labs-backpack']"
    add_to_cart_sauce_labs_bolt_t_shirt = "button[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
    add_to_cart_sauce_labs_onesie = "button[data-test='add-to-cart-sauce-labs-onesie']"
    to_shopping_cart = "a.shopping_cart_link"
    checkout_button = "button[name='checkout']"
    first_name_locator = "input#first-name"
    last_name_locator = "input#last-name"
    zip_code_locator = "input#postal-code"
    continue_locator = "input#continue"
    total_locator = "div.summary_total_label"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(open_url)
    driver.find_element(By.CSS_SELECTOR, username_locator).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, password_locator).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, login_button).click()

    driver.find_element(By.CSS_SELECTOR, add_to_cart_sauce_labs_backpack).click()
    driver.find_element(By.CSS_SELECTOR, add_to_cart_sauce_labs_bolt_t_shirt).click()
    driver.find_element(By.CSS_SELECTOR, add_to_cart_sauce_labs_onesie).click()
    driver.find_element(By.CSS_SELECTOR, to_shopping_cart).click()
    driver.find_element(By.CSS_SELECTOR, checkout_button).click()

    driver.find_element(By.CSS_SELECTOR, first_name_locator).send_keys(my_users_.firstname)
    driver.find_element(By.CSS_SELECTOR, last_name_locator).send_keys(my_users_.lastname)
    driver.find_element(By.CSS_SELECTOR, zip_code_locator).send_keys(my_users_.zip_code)
    driver.find_element(By.CSS_SELECTOR, continue_locator).click()

    return driver.find_element(By.CSS_SELECTOR, total_locator).text

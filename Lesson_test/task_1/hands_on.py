from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def hands_on(my_data_):
    open_url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    first_name_locator = "input[name='first-name']"
    last_name_locator = "input[name='last-name']"
    address_locator = "input[name='address']"
    email_locator = "input[name='e-mail']"
    phone_locator = "input[name='phone']"
    zip_locator = "input[name='zip-code']"
    city_locator = "input[name='city']"
    country_locator = "input[name='country']"
    job_locator = "input[name='job-position']"
    company_locator = "input[name='company']"
    submit_button = "button[type='submit']"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(open_url)

    driver.find_element(By.CSS_SELECTOR, first_name_locator).send_keys(my_data_.first_name)
    driver.find_element(By.CSS_SELECTOR, last_name_locator).send_keys(my_data_.last_name)
    driver.find_element(By.CSS_SELECTOR, address_locator).send_keys(my_data_.address)
    driver.find_element(By.CSS_SELECTOR, email_locator).send_keys(my_data_.email)
    driver.find_element(By.CSS_SELECTOR, phone_locator).send_keys(my_data_.phone)
    driver.find_element(By.CSS_SELECTOR, zip_locator).send_keys(my_data_.zip)
    driver.find_element(By.CSS_SELECTOR, city_locator).send_keys(my_data_.city)
    driver.find_element(By.CSS_SELECTOR, country_locator).send_keys(my_data_.country)
    driver.find_element(By.CSS_SELECTOR, job_locator).send_keys(my_data_.job)
    driver.find_element(By.CSS_SELECTOR, company_locator).send_keys(my_data_.company)
    driver.find_element(By.CSS_SELECTOR, submit_button).click()

    web_elements = driver.find_elements(By.CSS_SELECTOR, "div.row")

    return web_elements

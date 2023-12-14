from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_data_types():
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
    red_color = "rgba(132, 32, 41, 1)"
    green_color = "rgba(15, 81, 50, 1)"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(open_url)

    driver.find_element(By.CSS_SELECTOR, first_name_locator).send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, last_name_locator).send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, address_locator).send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, email_locator).send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, phone_locator).send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, zip_locator).send_keys("")
    driver.find_element(By.CSS_SELECTOR, city_locator).send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, country_locator).send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, job_locator).send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, company_locator).send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, submit_button).click()

    web_elements = driver.find_elements(By.CSS_SELECTOR, "div.row")

    zip_color = web_elements[4].find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
    first_name_color = web_elements[3].find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
    last_name_color = web_elements[3].find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")
    address_color = web_elements[4].find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")
    city_color = web_elements[4].find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")
    country_color = web_elements[4].find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")
    email_color = web_elements[5].find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")
    phone_color = web_elements[5].find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")
    job_color = web_elements[6].find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")
    company_color = web_elements[6].find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")

    assert zip_color == red_color
    assert first_name_color == green_color
    assert last_name_color == green_color
    assert address_color == green_color
    assert  city_color == green_color
    assert country_color == green_color
    assert email_color == green_color
    assert phone_color == green_color
    assert job_color == green_color
    assert company_color == green_color

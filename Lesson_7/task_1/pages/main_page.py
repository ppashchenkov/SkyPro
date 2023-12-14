from selenium.webdriver.common.by import By
from hands_data import HandsData


class MainPage:
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
    web_elements = ""
    red_color = "rgba(132, 32, 41, 1)"
    green_color = "rgba(15, 81, 50, 1)"

    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.get(self.open_url)

    def enter_data(self, my_data):
        self._driver.find_element(By.CSS_SELECTOR, self.first_name_locator).send_keys(my_data.first_name)
        self._driver.find_element(By.CSS_SELECTOR, self.last_name_locator).send_keys(my_data.last_name)
        self._driver.find_element(By.CSS_SELECTOR, self.address_locator).send_keys(my_data.address)
        self._driver.find_element(By.CSS_SELECTOR, self.email_locator).send_keys(my_data.email)
        self._driver.find_element(By.CSS_SELECTOR, self.phone_locator).send_keys(my_data.phone)
        self._driver.find_element(By.CSS_SELECTOR, self.zip_locator).send_keys(my_data.zip)
        self._driver.find_element(By.CSS_SELECTOR, self.city_locator).send_keys(my_data.city)
        self._driver.find_element(By.CSS_SELECTOR, self.country_locator).send_keys(my_data.country)
        self._driver.find_element(By.CSS_SELECTOR, self.job_locator).send_keys(my_data.job)
        self._driver.find_element(By.CSS_SELECTOR, self.company_locator).send_keys(my_data.company)

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, self.submit_button).click()
        self.web_elements = self._driver.find_elements(By.CSS_SELECTOR, "div.row")

    def is_zip(self):
        zip_color = self.web_elements[4].find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
        if zip_color == self.red_color:
            return True

        # first_name_color = web_elements[3].find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
        # last_name_color = web_elements[3].find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")
        # address_color = web_elements[4].find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")
        # city_color = web_elements[4].find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")
        # country_color = web_elements[4].find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")
        # email_color = web_elements[5].find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")
        # phone_color = web_elements[5].find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")
        # job_color = web_elements[6].find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")
        # company_color = web_elements[6].find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")

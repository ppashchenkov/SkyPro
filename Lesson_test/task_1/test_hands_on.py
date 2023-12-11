import pytest
from selenium.webdriver.common.by import By
from hands_data import HandsData
from hands_on import hands_on

my_data = HandsData("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва",
                    "Россия", "QA", "SkyPro")


@pytest.mark.parametrize('my_data_, red_, green_', [
    (my_data, "rgba(132, 32, 41, 1)", "rgba(15, 81, 50, 1)")
])
def test_hands_on_zip(my_data_, red_, green_):
    green_list = ['first_color', 'last_color', 'address_color', 'city_color', 'country_color',
                  'email_color', 'phone_color', 'job_color', 'company_color']
    green_result = True

    web_data = hands_on(my_data)

    zip_color = web_data[4].find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
    green_list[0] = web_data[3].find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")
    green_list[1] = web_data[3].find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")
    green_list[2] = web_data[4].find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")
    green_list[3] = web_data[4].find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")
    green_list[4] = web_data[4].find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")
    green_list[5] = web_data[5].find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")
    green_list[6] = web_data[5].find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")
    green_list[7] = web_data[6].find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")
    green_list[8] = web_data[6].find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")

    for green in green_list:
        if green != green_: green_result = False

    assert zip_color == red_ and green_result

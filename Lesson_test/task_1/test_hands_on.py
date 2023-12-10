import pytest
from selenium.webdriver.common.by import By
from hands_data import HandsData
from hands_on import hands_on

my_data = HandsData("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва",
                    "Россия", "QA", "SkyPro")


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(132, 32, 41, 1)")
    ])
def test_hands_on_zip(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[4].find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")

    assert res == res_


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(15, 81, 50, 1)")
    ])
def test_hands_first_name(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[3].find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("color")

    assert res == res_


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(15, 81, 50, 1)")
    ])
def test_hands_on_last_name(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[3].find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("color")

    assert res == res_


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(15, 81, 50, 1)")
    ])
def test_hands_on_address(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[4].find_element(By.CSS_SELECTOR, "#address").value_of_css_property("color")

    assert res == res_


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(15, 81, 50, 1)")
    ])
def test_hands_on_city(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[4].find_element(By.CSS_SELECTOR, "#city").value_of_css_property("color")

    assert res == res_


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(15, 81, 50, 1)")
    ])
def test_hands_on_country(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[4].find_element(By.CSS_SELECTOR, "#country").value_of_css_property("color")

    assert res == res_


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(15, 81, 50, 1)")
    ])
def test_hands_on_email(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[5].find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("color")

    assert res == res_


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(15, 81, 50, 1)")
    ])
def test_hands_on_phone(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[5].find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("color")

    assert res == res_


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(15, 81, 50, 1)")
    ])
def test_hands_on_job(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[6].find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("color")

    assert res == res_


@pytest.mark.parametrize('my_data_, res_', [
    (my_data, "rgba(15, 81, 50, 1)")
    ])
def test_hands_on_company(my_data_, res_):
    web_data = hands_on(my_data)
    res = web_data[6].find_element(By.CSS_SELECTOR, "#company").value_of_css_property("color")

    assert res == res_

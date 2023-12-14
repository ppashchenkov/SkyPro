from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from main_page_task1 import MainPage
from datas import MyData


def test_valid_data():
    my_data = MyData("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва",
                        "Россия", "QA", "SkyPro")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.enter_data(my_data)
    main_page.submit()

    assert main_page.is_zip()
    assert main_page.is_first_name()
    assert main_page.is_last_name()
    assert main_page.is_address()
    assert main_page.is_city()
    assert main_page.is_country()
    assert main_page.is_email()
    assert main_page.is_phone()
    assert main_page.is_job()
    assert main_page.is_company()

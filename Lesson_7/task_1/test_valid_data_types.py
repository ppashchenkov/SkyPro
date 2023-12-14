from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.hands_data import HandsData
from pages.main_page import MainPage


def test_valid_data():
    my_data = HandsData("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва",
                        "Россия", "QA", "SkyPro")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.enter_data(my_data)
    main_page.submit()

    assert main_page.is_zip()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from main_page import MainPage


def calculator(_delay):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.set_delay()
    main_page.get_7_plus_8()
    return main_page.get_result(_delay)


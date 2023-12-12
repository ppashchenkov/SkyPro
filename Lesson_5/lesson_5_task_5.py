from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

open_url = "http://uitestingplayground.com/classattr"
blue_button = ".btn-primary"

browsers = [webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
            webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            ]

for browser in browsers:
    driver = browser
    driver.maximize_window()
    driver.get(open_url)

    try:
        for i in range(0,3):
            driver.find_element(By.CSS_SELECTOR, blue_button).click()
            EC.alert_is_present()
            driver.switch_to.alert.accept()
            print(f"Нажал на синюю кнопку {i+1}-й раз")
    except:
        print("Не  смог нажать на синюю кнопку 3 раза")

    driver.quit()

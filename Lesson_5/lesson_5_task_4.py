from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

open_url = "http://uitestingplayground.com/dynamicid"
blue_button = "//button[contains(@class, 'btn')]"

browsers = [webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
            webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            ]

for browser in browsers:
    driver = browser
    driver.maximize_window()
    driver.get(open_url)

    try:
        for i in range(0,3):
            driver.find_element(By.XPATH, blue_button).click()
            print(f"Нажали синюю кнопку {i+1} раз(а)")
    except:
        print("Не удалось нажать 3 раза синюю кнопку!")
    driver.quit()

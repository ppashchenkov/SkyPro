from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

open_url = "http://uitestingplayground.com/dynamicid"
blue_button = "//button[contains(@class, 'btn')]"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(open_url)

try:
    for i in range(0,3):
        driver.find_element(By.XPATH, blue_button).click()
        print(f"Нажали синюю кнопку {i+1} раз(а)")
except:
    print("Не удалось нажать 3 раза синюю кнопку!")

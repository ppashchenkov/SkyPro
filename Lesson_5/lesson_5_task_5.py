from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

open_url = "http://uitestingplayground.com/classattr"
blue_button = ".btn-primary"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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




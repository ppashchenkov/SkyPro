from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


open_url = "http://uitestingplayground.com/ajax"
blue_button = "#ajaxButton"
green_text = "p.bg-success"

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.maximize_window()
waiter20 = WebDriverWait(driver, 2)

driver.get(open_url)
driver.find_element(By.CSS_SELECTOR, blue_button).click()
waiter20.until(EC.visibility_of_element_located((By.CSS_SELECTOR, green_text)))
print(driver.find_element(By.CSS_SELECTOR, green_text).text)
driver.quit()
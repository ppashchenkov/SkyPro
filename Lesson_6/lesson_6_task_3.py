from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

open_url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
done = (By.ID, "text")
img_container = "img"

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()
driver.maximize_window()
waiter30 = WebDriverWait(driver, 30)

driver.get(open_url)
waiter30.until(EC.text_to_be_present_in_element(done, "Done!"))
lst = driver.find_elements(By.CSS_SELECTOR, img_container)

print(lst[3].get_attribute("src"))
driver.quit()
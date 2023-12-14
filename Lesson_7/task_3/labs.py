from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from authorization_page import AuthPage
from main_page import MainPage
from cart_page import CartPage
from info_page import InfoPage
from checkout_page import CheckoutPage

def labs_shopping():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    auth = AuthPage(driver)
    auth.authorization()

    main = MainPage(driver)
    main.add_items_to_cart()
    main.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    info = InfoPage(driver)
    info.enter_your_details()

    checkout = CheckoutPage(driver)
    return checkout.get_total()



from saucedemo_task.pages.home_page import Home_page
from saucedemo_task.pages.product_page import Product_page
from saucedemo_task.pages.cart_page import Cart_page
from saucedemo_task.pages.your_information_page import YOUR_INFORMATION_PAGE
from saucedemo_task.pages.checkout_overview_page import Checkout_page
from saucedemo_task.pages.finished_order_page import Finished_order_page
from faker import Faker
fake = Faker()
fake_JP = Faker('ja_JP')
name_of_last_product = ""
name_of_penultimate_product = ''

def test_home_page(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    home_page = Home_page(driver=driver)
    home_page.enter_login_and_password('standard_user', 'secret_sauce')
    home_page.click_to_LoginButton()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_product_page(driver):
    product_page = Product_page(driver=driver)
    product_page.add_last_two_items_to_cart()
    product_page.click_on_curt_button()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"
    global name_of_last_product
    name_of_last_product = product_page.name_of_lust_product()
    global name_of_penultimate_product
    name_of_penultimate_product = product_page.name_of_penultimate_product()
    assert name_of_penultimate_product == "Test.allTheThings() T-Shirt (Red)"

def test_curt_page(driver):
    cart_page = Cart_page(driver=driver)
    assert len(cart_page.list_of_items()) == 2
    global name_of_penultimate_product
    global name_of_last_product
    assert name_of_penultimate_product + name_of_last_product == cart_page.first_item_in_cart().text + cart_page.second_item_in_cart().text
    cart_page.remove_product_from_cart(cart_page.second_item_in_cart().text)
    assert len(cart_page.list_of_items()) == 1
    cart_page.click_checkout_button()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

def test_your_information_page(driver):
    information_page = YOUR_INFORMATION_PAGE(driver=driver)
    information_page.enter_first_name(fake_JP.unique.first_name())
    information_page.enter_last_name(fake.unique.first_name())
    information_page.enter_postal_code(fake.ean())
    information_page.click_on_continue_button()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

def test_checkout_summary_overview(driver):
    checkout_page = Checkout_page(driver=driver)
    checkout_page.click_finish_button()

    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"



def test_finished_order_page(driver):
    finish_page = Finished_order_page(driver)
    assert finish_page.get_checkout_header_text() == "THANK YOU FOR YOUR ORDER"
    finish_page.click_back_home_button()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"




from selenium.webdriver.common.by import By

CART_ITEMS_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")

def remove_button_of_selected_item(name_of_product: str):
    name = name_of_product.lower().replace(' ', '-')
    LOCATOR = (By.XPATH, f"//button[@id='remove-{name}']")
    return LOCATOR

CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")
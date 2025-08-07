from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from end_to_end_pyTest.browserUtils.utils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        self.cart_checkout_btn = (By.CSS_SELECTOR, "a[class*='nav-link btn']")
        self.wait = WebDriverWait(self.driver, 10)

    def shop_link_action(self):
        self.driver.find_element(*self.shop_link).click()

    def add_product(self, product_name):
        print(self.getTitle())
        cart_btn_xpath = "//a[contains(text(),'" + product_name + "')]//ancestor::div[@class='card h-100']/div/button"
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, cart_btn_xpath)))
        products = self.driver.find_elements(By.XPATH, cart_btn_xpath)
        print(products)
        for cart in products:
            cart.click()

    def cart_checkout(self):
        cart_btn = self.wait.until(expected_conditions.element_to_be_clickable(self.cart_checkout_btn))
        cart_btn.click()


import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from end_to_end_pyTest.browserUtils.utils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, "a[href*='shop']")
        #self.cart_checkout_btn = (By.CSS_SELECTOR, "a[class*='nav-link btn']") not working in CLI
        self.cart_checkout_btn = (By.XPATH, "//a[contains(text(), 'Checkout')]")
        self.wait = WebDriverWait(self.driver, 20)

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
        print("Checking out cart...")
        self.wait.until(expected_conditions.presence_of_element_located(self.cart_checkout_btn))
        element = self.driver.find_element(*self.cart_checkout_btn)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element)
        # Optional: wait after scroll
        time.sleep(1)
        print("Displayed:", element.is_displayed())
        print("Enabled:", element.is_enabled())
        if element.is_displayed() and element.is_enabled():
            cart_btn = self.wait.until(expected_conditions.element_to_be_clickable(self.cart_checkout_btn))
            cart_btn.click()
        else:
            # Added to fix disable button to click in CLI mode
            self.driver.execute_script("arguments[0].click();", element)

        print("Cart checkout clicked.")

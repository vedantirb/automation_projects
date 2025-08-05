from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from end_to_end_pyTest.browserUtils.utils import BrowserUtils


class ProductPurchase(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_btn = (By.XPATH, "//button[contains(text(), 'Checkout')]")
        self.country_txt = (By.CSS_SELECTOR, "input[class*='filter-input']")
        self.terms_chkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.purchase_btn = (By.XPATH, "//input[@value='Purchase']")
        self.alert_success = (By.CSS_SELECTOR, "div[class*='alert-success']")
        self.wait = WebDriverWait(self.driver, 10)


    def checkout_action(self):
        print(self.getTitle())
        self.driver.find_element(*self.checkout_btn).click()

    def add_address(self, country):
        self.driver.find_element(*self.country_txt).send_keys(country)
        country_txt = (By.LINK_TEXT, country)
        self.wait.until(expected_conditions.presence_of_element_located(country_txt))
        self.driver.find_element(*country_txt).click()
        self.driver.find_element(*self.terms_chkBox).click()

    def confirm_purchase(self):
        self.driver.find_element(*self.purchase_btn).click()

    def validate_purchase(self):
        success_msg = self.driver.find_element(*self.alert_success).text

        assert "Success! Thank you!" in success_msg

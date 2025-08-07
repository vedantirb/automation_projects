from selenium.webdriver.common.by import By

from end_to_end_pyTest.browserUtils.utils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.NAME, "password")
        self.admin = (By.CSS_SELECTOR, "input[value='admin']")
        self.term = (By.XPATH, "//input[@id='terms']")
        self.signIn = (By.XPATH, "//input[@id='signInBtn']")
        self.alert_label =(By.XPATH, "//div[contains(@class,'alert-danger')]")

    def login(self, username, password):
        print(self.getTitle())
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.admin).click()
        self.driver.find_element(*self.term).click()
        self.driver.find_element(*self.signIn).click()

    def login_message(self):
        return self.driver.find_element(*self.alert_label).text



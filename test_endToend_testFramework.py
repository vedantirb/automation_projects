'''
Test cases
'''

import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from end_to_end_pyTest.pageObject.loginPage import LoginPage
from end_to_end_pyTest.pageObject.productPurchase import ProductPurchase
from end_to_end_pyTest.pageObject.shopPage import ShopPage
#from selenium.common.exceptions import NoAlertPresentException

data_input_file = "dataInputs/inputs.json"
with open(data_input_file) as input_file:
    input_data = json.load(input_file)

@pytest.mark.parametrize("testData", input_data["TestData"])
def test_end2end(webDriver, testData):
    driver = webDriver
    #driver.get("https://rahulshettyacademy.com/angularpractice/")

    loginPg = LoginPage(driver)
    loginPg.login(testData["username"], testData["password"])

    shopPg = ShopPage(driver)
    shopPg.shop_link_action()
    shopPg.add_product(testData["product_name"])
    shopPg.cart_checkout()

    purchasePg = ProductPurchase(driver)
    purchasePg.checkout_action()
    purchasePg.add_address("India")
    purchasePg.confirm_purchase()
    purchasePg.validate_purchase()

    # password_popup = wait.until(expected_conditions.element_to_be_clickable((By.ID, "okayBtn")))
    # password_popup.click()
    # wait.until(expected_conditions.alert_is_present())
    # try:
    #     alert = driver.switch_to.alert
    #     print(alert.text)
    #     alert.accept()
    # except:
    #     print("No alert present")
    #driver.execute_script("document.getElementById('okayBtn').click()")
    # driver.execute_script("document.querySelector('.modal').remove();")

list1=[1,2,3]




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

    loginPg = LoginPage(driver)
    loginPg.login(testData["username"], testData["password"])

    if "Incorrect" in loginPg.login_message():
        return None

    shopPg = ShopPage(driver)
    print("Navigating to shop...")
    shopPg.shop_link_action()

    print(f"Adding product: {testData['product_name']}")
    shopPg.add_product(testData["product_name"])


    print("Clicking on cart checkout button...")
    try:
        shopPg.cart_checkout()
    except Exception as e:
        print(f"❌ Cart checkout failed: {e}")
        # Take manual screenshot for CI debugging
        driver.save_screenshot("./reports/checkout_failure.png")
        raise

    purchasePg = ProductPurchase(driver)
    purchasePg.checkout_action()
    purchasePg.add_address("India")
    purchasePg.confirm_purchase()
    purchasePg.validate_purchase()






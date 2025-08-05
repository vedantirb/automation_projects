import pytest

from selenium.webdriver.common.by import By

@pytest.mark.sort
def test_sortTable(webDriver):
    driver = webDriver
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.find_element(By.LINK_TEXT, "Top Deals").click()

    all_win = driver.window_handles
    driver.switch_to.window(all_win[1])
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
    items = []
    deal_item_list = driver.find_elements(By.XPATH, "//tbody//tr/td[1]")
    for each in deal_item_list:
        items.append(each.text)

    sorted_items = sorted(items)
    assert sorted_items == items
    print("Items already sorted correctly")
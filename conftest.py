import datetime
import os
import time
import tempfile
import shutil

import pytest
from pygments.lexer import default
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


#browser_name = "chrome"

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Define browser name to run")



@pytest.fixture(scope="function")
def webDriver(request):

    browser_name = request.config.getoption("--browser_name")
    print(f"browser_name selected:{browser_name}")
    driver = None
    option = Options()
    # Create a unique temporary directory for user data
    user_data_dir = tempfile.mkdtemp()
    
    option.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_settings.popups": False
    })

    option.add_argument("--disable-popup-blocking")
    option.add_argument("--disable-notifications")
    option.add_argument("--disable-infobars")
    option.add_argument(f"--user-data-dir={user_data_dir}")
    option.add_argument("--disable-blink-features=AutomationControlled")
    option.add_argument("--disable-features=PasswordLeakDetection")
    option.add_argument("--incognito")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")

    if browser_name == "chrome":
        driver = webdriver.Chrome(options=option)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie(options=option)
    elif browser_name == "Edge":
        driver = webdriver.Edge(options=option)
    else:
        print(f"Invalid Driver name {browser_name}")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()
    # Clean up the temporary user data directory
    shutil.rmtree(user_data_dir, ignore_errors=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("webDriver", None)
        if driver:
            screenshot_base64 = driver.get_screenshot_as_base64()

            if hasattr(rep, "extra"):
                rep.extra.append(extras.image(screenshot_base64, mime_type="image/png"))
            else:
                rep.extra = [extras.image(screenshot_base64, mime_type="image/png")]

'''
save screenshot with in project screenshot dir
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("webDriver", None)
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            test_name = item.name
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filepath = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")

            driver.save_screenshot(filepath)
            print(f"\nScreenshot saved: {filepath}")

            # Attach screenshot to the html report
            if hasattr(rep, "extra"):
                rep.extra.append(extras.image(filepath))
            else:
                rep.extra = [extras.image(filepath)]
'''


import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(autouse=True)
def driver():
    driver=WebDriver()
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

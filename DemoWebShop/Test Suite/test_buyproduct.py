from selenium.webdriver import ActionChains
from DemoWebShop.POM.buy_product import Buy_product

def test_buyproduct(driver):
    sign_page_obj=Buy_product(driver,ActionChains)
    sign_page_obj.buy_product("reddyvinuth27@gmail.com","selenium")

    assert driver.find_element("xpath","//a[.='Register']").is_displayed()


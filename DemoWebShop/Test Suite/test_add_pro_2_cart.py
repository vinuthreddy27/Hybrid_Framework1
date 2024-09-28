from selenium.webdriver import ActionChains

from DemoWebShop.POM.add_product_2_cart import Add_2_cart


def test_add_product_to_cart(driver):
    add_product_page_obl=Add_2_cart(driver,ActionChains)
    add_product_page_obl.add_2_cart("reddyvinuth27@gmail.com","selenium")

    assert driver.find_element("xpath", "//a[.='Register']").is_displayed()

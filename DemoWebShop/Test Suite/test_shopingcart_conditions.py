from selenium.webdriver import ActionChains
from DemoWebShop.POM.shopping_cart import Shopping_cart


def test_shopping_cart(driver):
    shopping_cart_obj=Shopping_cart(driver,ActionChains)
    shopping_cart_obj.shopping_cart("reddyvinuth27@gmail.com","selenium","4")

    assert driver.find_element("xpath", "//div[@class='topic-html-content-title']").is_displayed()

from selenium.webdriver import ActionChains
from DemoWebShop.POM.wishlist import Wishlist


def test_wishlist(driver):
    wishlist_page_obj=Wishlist(driver,ActionChains)
    wishlist_page_obj.wishlist("reddyvinuth27@gmail.com","selenium","0")


    assert driver.find_element("xpath", "//div[@class='topic-html-content-title']").is_displayed()

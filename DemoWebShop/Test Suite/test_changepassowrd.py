from selenium.webdriver import ActionChains
from DemoWebShop.POM.changepasswordpage import Change_passowrd


def test_change_password(driver):
    review_page_obj=Change_passowrd(driver,ActionChains)
    review_page_obj.change_password("rv115@gmail.com",
                                    "rv115@gmail.com",
                                    "framework1",
                                    "framework1",
                                    "framework",
                                    "framework")


    assert driver.find_element("xpath", "//div[@class='topic-html-content-title']").is_displayed()

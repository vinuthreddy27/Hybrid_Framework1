import pytest
from selenium.webdriver import ActionChains
from DemoWebShop.POM.emailfriendpage import Email


def test_email(driver):
    review_page_obj=Email(driver,ActionChains)
    review_page_obj.email_friend("reddyvinuth27@gmail.com",
                           "selenium",
                           "abc")
    assert driver.find_element("xpath", "//div[@class='topic-html-content-title']").is_displayed()


def test_email2(driver):
    review_page_obj=Email(driver,ActionChains)
    review_page_obj.email_valid_mail_friend("reddyvinuth27@gmail.com",
                           "selenium",
                           "abc@gmail.com",
                           "shedg baa kunte bille hadam....")

    assert driver.find_element("xpath", "//div[@class='topic-html-content-title']").is_displayed()

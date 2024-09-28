from selenium.webdriver import ActionChains

from DemoWebShop.POM.reviewpage import Review

def test_review(driver):
    review_page_obj=Review(driver,ActionChains)
    review_page_obj.review("reddyvinuth27@gmail.com",
                           "selenium",
                           "Diamond Heart",
                           "good product value for money")

    assert driver.find_element("xpath", "//div[@class='topic-html-content-title']").is_displayed()


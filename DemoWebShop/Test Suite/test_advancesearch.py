from selenium.webdriver import ActionChains
from DemoWebShop.POM.advancesearch import Advance_search

def test_advance_search(driver):
    advance_seach_obj=Advance_search(driver,ActionChains)
    advance_seach_obj.advance_search("reddyvinuth27@gmail.com","reddyvinuth27@gmail.com","selenium","shoe")


    assert driver.find_element("xpath","//div[@class='topic-html-content-title']").is_displayed()
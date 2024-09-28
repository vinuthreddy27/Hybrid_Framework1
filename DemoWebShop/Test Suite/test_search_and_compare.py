from selenium.webdriver import ActionChains
from DemoWebShop.POM.search_and_compare import Search_and_compare



def test_seach_and_compare(driver):
    seach_and_compare_page_obj=Search_and_compare(driver,ActionChains)
    seach_and_compare_page_obj.search_and_compare("reddyvinuth27@gmail.com","selenium")

    assert driver.find_element("xpath", "//div[@class='page-body']").is_displayed()
    assert driver.find_element("xpath", "//div[@class='topic-html-content-title']").is_displayed()
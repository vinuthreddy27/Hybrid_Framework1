from selenium.webdriver import ActionChains
from DemoWebShop.POM.filter_conditionpage import Filter_condtion


def test_filter_condition(driver):
    filter_c_page_obj=Filter_condtion(driver,ActionChains)
    filter_c_page_obj.filter_conditions("reddyvinuth27@gmail.com","selenium")

    assert driver.find_element("xpath","//div[@class='topic-html-content-title']").is_displayed()




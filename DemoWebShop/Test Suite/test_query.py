from selenium.webdriver import ActionChains
from DemoWebShop.POM.querypage import Query




def test_query(driver):
    query_page_obj=Query(driver,ActionChains)
    query_page_obj.query("reddyvinuth27@gmail.com","reddyvinuth27@gmail.com",
                         "selenium",
                         "in the application where we are enable to find add to cart button"
                         "for some products....")
    assert driver.find_element("xpath","//div[@class='topic-html-content-title']").is_displayed()
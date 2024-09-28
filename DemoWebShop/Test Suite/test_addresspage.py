from selenium.webdriver import ActionChains
from DemoWebShop.POM.addresspage import Address

def test_address(driver):
    address_page_obj=Address(driver,ActionChains)
    address_page_obj.address("reddyvinuth27@gmail.com","reddyvinuth27@gmail.com",
                             "selenium",
                             "vinuth",
                             "reddy",
                             "reddyvinuth27@gmail.com",
                             "Bengaluru",
                             "111 1st cross",
                             "BTM",
                             "560100",
                             "9191919191",
                             "mysuru")

    assert driver.find_element("xpath","//div[@class='topic-html-content-title']").is_displayed()
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from DemoWebShop.POM.search import Subscribe

credentials=[("Copy of Computing and Internet EX"),
             ("Build your own expensive computer"),
             ("friction"),
             ("blue jeans"),
             ("blue sneakers"),
             ("Camcorder"),
             ("Smartphone")]


@pytest.mark.parametrize("products",credentials)
def test_subscribe(driver,products):
   subscribe_page_obj = Subscribe(driver,ActionChains)
   subscribe_page_obj.sub_scibe("reddyvinuth27@gmail.com","selenium",
                                products)

   allure.attach(driver.get_screenshot_as_png(),
                   name="test_subscribe.png",
                   attachment_type=AttachmentType.PNG)

   assert driver.find_element("xpath", "//div[@class='topic-html-content-title']").is_displayed()


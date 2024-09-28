import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from DemoWebShop.POM.register import Register

def test_register_with_valid_credentials(driver):
    home=Register(driver,ActionChains)
    home.register_into_application_m("demo",
                                       "web123",
                                       "xyz@1234",
                                       "xyz@1234")
    condition=driver.find_element("xpath","//div[@class='topic-html-content-title']").is_displayed()

    if condition==True:
      allure.attach(driver.get_screenshot_as_png(),
                  name="test_register.png",
                  attachment_type=AttachmentType.PNG)


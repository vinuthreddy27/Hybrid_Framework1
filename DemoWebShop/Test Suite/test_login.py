import pytest
# from DemoWebShop.Utilities.exel_reader import get_list_from_excel
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from DemoWebShop.POM.login import Login
import allure

# credentials = get_list_from_excel()

credentials=[("reddyvinuth27@gmail.com","selenium"),
             ("rv115@gmail.com","framework1"),
             ("jyothithakkur03@gmail.com","selenium")]

@pytest.mark.parametrize("email,password",credentials)
def test_login_valid_credentials(driver,email,password):
    login_Page_obj =Login(driver,ActionChains)
    login_Page_obj.login(email,password)

    condition=driver.find_element("xpath",f"//a[.='{email}']").is_displayed()
    if condition==True:
        allure.attach(driver.get_screenshot_as_png(),
                  name="test_login_valid_credentials.png",
                  attachment_type=AttachmentType.PNG)




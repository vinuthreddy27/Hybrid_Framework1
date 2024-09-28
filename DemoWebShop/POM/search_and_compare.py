from DemoWebShop.lib.library import Base
from time import sleep

class Search_and_compare(Base):
    login_link_locator = ("xpath", "//a[.='Log in']")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
    ele_locator = ("xpath", "//a[@href='/electronics']")
    camera_photo_locator=("xpath","//img[@alt='Picture for category Camera, photo']")
    product_locator=("xpath", "//h2[@class='product-title']/.//a[@href='/hard-drive-handycam-camcorder']")
    add_compare_btn=("xpath", "//input[@value='Add to compare list']")
    product_locator_2=("xpath", "//h2[@class='product-title']/.//a[@href='/camcorder']")
    add_compare_btn2=("xpath", "//input[@value='Add to compare list']")
    remove_btn=("xpath", "//img[@alt='Picture of Camcorder']/../..//input[@value='Remove']")
    remove_btn2=("xpath", "//img[contains(@alt,'1MP 60GB Hard')]/../..//input[@value='Remove']")
    logout_locator = ("xpath", "//li[.='Log out']")

    def search_and_compare(self,email,password):
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator, email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.click_on_a_element(self.ele_locator)
        self.click_on_a_element(self.camera_photo_locator)
        self.click_on_a_element(self.product_locator)
        self.click_on_a_element(self.add_compare_btn)
        self.navigational_commands()
        self.navigational_commands()
        self.click_on_a_element(self.product_locator_2)
        self.click_on_a_element(self.add_compare_btn2)
        self.click_on_a_element(self.remove_btn)
        self.click_on_a_element(self.remove_btn2)
        self.click_on_a_element(self.logout_locator)


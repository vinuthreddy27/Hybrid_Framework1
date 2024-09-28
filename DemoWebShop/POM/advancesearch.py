from time import sleep
from DemoWebShop.lib.library import Base

class Advance_search(Base):
    subscribe_locater = ("id", "newsletter-email")
    subscribe_btn = ("id", "newsletter-subscribe-button")
    login_link_locator = ("xpath", "//a[.='Log in']")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
    search_locator=("xpath","//a[.='Search']")
    search_keyword_locator = ("id","Q")
    search_btn = ("xpath", "//input[@value='Search']")
    advance_search_locator=("id","As")
    select_locator=("id","Cid")
    opton_locator=("xpath","//option[.='Books']")
    search_btn2=("xpath","//input[@value='Search']")
    logout_locator=("xpath","//a[.='Log out']")

    def advance_search(self,mail,email,password,shoe):
        self.send_keys_to_text_field(self.subscribe_locater,mail)
        self.click_on_a_element(self.subscribe_btn)
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator, email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.click_on_a_element(self.search_locator)
        self.send_keys_to_text_field(self.search_keyword_locator,shoe)
        self.click_on_a_element(self.advance_search_locator)
        self.select_a_option(self.select_locator, self.opton_locator)
        self.click_on_a_element(self.search_btn2)
        self.dismiss_an_alert()
        self.click_on_a_element(self.logout_locator)



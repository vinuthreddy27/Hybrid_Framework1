from DemoWebShop.lib.library import Base

class Subscribe(Base):
    subscribe_locater=("id","newsletter-email")
    subscribe_btn = ("id", "newsletter-subscribe-button")
    login_link_locator = ("xpath", "//a[.='Log in']")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
    search_text_field_locator = ("id", "small-searchterms")
    search_btn = ("xpath", "//input[@value='Search']")
    logout_locator=("xpath","//li[.='Log out']")

    def sub_scibe(self,email,password,product):
        self.send_keys_to_text_field(self.subscribe_locater,email)
        self.click_on_a_element(self.subscribe_btn)
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator, email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.send_keys_to_text_field(self.search_text_field_locator,product)
        self.click_on_a_element(self.search_btn)
        self.click_on_a_element(self.logout_locator)

from DemoWebShop.lib.library import Base
from time import sleep
class Query(Base):
    subscribe_locater = ("id", "newsletter-email")
    subscribe_btn = ("id", "newsletter-subscribe-button")
    login_link_locator = ("xpath", "//a[.='Log in']")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
    contact_us_locator=("xpath","//a[.='Contact us']")
    enquery_textfield_locator=("id","Enquiry")
    submit_btn_locator=("xpath","//input[@name='send-email']")
    logout_locator=("xpath","//li[.='Log out']")


    def query(self,mail,email,password,query):
        self.send_keys_to_text_field(self.subscribe_locater, mail)
        self.click_on_a_element(self.subscribe_btn)
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator, email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.click_on_a_element(self.contact_us_locator)
        self.send_keys_to_text_field(self.enquery_textfield_locator,query)
        self.click_on_a_element(self.submit_btn_locator)
        self.click_on_a_element(self.logout_locator)

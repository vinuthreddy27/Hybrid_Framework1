from DemoWebShop.lib.library import Base

class Email(Base):
    login_link_locator = ("xpath", "//a[.='Log in']")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
    logout_locator=("xpath","//li[.='Log out']")
    ele_locator=("xpath","//div[@class='header-menu']/.//a[@href='/electronics']")
    image_locator=("xpath","//img[@alt='Picture for category Cell phones']")
    product_locator=("xpath","//div[@class='picture']/..//a[.='Smartphone']")
    email_a_friend_locator=("xpath","//input[@value='Email a friend']")
    text_locator=("id","PersonalMessage")
    friend_email_locator=("id","FriendEmail")
    send_mail_locator=("name","send-email")

    def email_friend(self,email,password,mail):
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator, email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.click_on_a_element(self.ele_locator)
        self.click_on_a_element(self.image_locator)
        self.click_on_a_element(self.product_locator)
        self.click_on_a_element(self.email_a_friend_locator)
        self.send_keys_to_text_field(self.friend_email_locator,mail)
        self.click_on_a_element(self.send_mail_locator)
        self.send_keys_to_text_field(self.friend_email_locator,mail)
        self.click_on_a_element(self.logout_locator)


    def email_valid_mail_friend(self,email,password,mail,text):
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator, email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.click_on_a_element(self.ele_locator)
        self.click_on_a_element(self.image_locator)
        self.click_on_a_element(self.product_locator)
        self.click_on_a_element(self.email_a_friend_locator)
        self.send_keys_to_text_field(self.friend_email_locator,mail)
        self.send_keys_to_text_field(self.text_locator,text)
        self.click_on_a_element(self.send_mail_locator)
        self.click_on_a_element(self.logout_locator)



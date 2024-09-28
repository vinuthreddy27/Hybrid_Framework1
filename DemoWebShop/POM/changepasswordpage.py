from DemoWebShop.lib.library import Base


class Change_passowrd(Base):
    subscribe_locater = ("id", "newsletter-email")
    subscribe_btn = ("id", "newsletter-subscribe-button")
    login_link_locator = ("xpath", "//a[.='Log in']")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
    myaccount_locator=("xpath","//a[.='My account']")
    change_password_locator=("xpath","//a[.='Change password']")
    old_password_locator=("name","OldPassword")
    new_password_locator=("name","NewPassword")
    conform_password_locator=("id","ConfirmNewPassword")
    change_password_btn=("xpath","//input[@value='Change password']")
    logout_locator=("xpath","//a[.='Log out']")


    def change_password(self,mail,email,password,text1,text2,text3):
        self.send_keys_to_text_field(self.subscribe_locater,mail)
        self.click_on_a_element(self.subscribe_btn)
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator, email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.click_on_a_element(self.myaccount_locator)
        self.click_on_a_element(self.change_password_locator)
        self.send_keys_to_text_field(self.old_password_locator,text1)
        self.send_keys_to_text_field(self.new_password_locator,text2)
        self.send_keys_to_text_field(self.conform_password_locator,text3)
        self.click_on_a_element(self.change_password_btn)
        self.click_on_a_element(self.logout_locator)

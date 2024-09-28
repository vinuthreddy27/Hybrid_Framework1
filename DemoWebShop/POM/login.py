from DemoWebShop.lib.library import Base
from DemoWebShop.Utilities.locatorsHub import LoginPageLocators

class Login(Base):
    def login(self,email,password):
        self.click_on_a_element(LoginPageLocators.login_link_locator)
        self.send_keys_to_text_field(LoginPageLocators.email_locator,email)
        self.send_keys_to_text_field(LoginPageLocators.password_locator,password)
        self.click_on_a_element(LoginPageLocators.login_btn)
        # self.click_on_a_element(LoginPageLocators.logout_locator)


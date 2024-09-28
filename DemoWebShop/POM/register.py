from DemoWebShop.lib.library import Base
from DemoWebShop.Utilities.locatorsHub import RegisterPageLocators
class Register(Base):

    def register_into_application_m(self,username,lastname,password,c_password):
        self.click_on_a_element(RegisterPageLocators.register_link_locater)
        self.click_on_a_element(RegisterPageLocators.male_radio_btn)
        self.send_keys_to_text_field(RegisterPageLocators.first_name_locator,username)
        self.send_keys_to_text_field(RegisterPageLocators.last_name_locator,lastname)
        self.send_keys_to_text_field(RegisterPageLocators.email_locater, self.generate_random_email())
        self.send_keys_to_text_field(RegisterPageLocators.password_locator,password)
        self.send_keys_to_text_field(RegisterPageLocators.conform_password_locator,c_password)
        self.click_on_a_element(RegisterPageLocators.register_btn)
        self.click_on_a_element(RegisterPageLocators.continue_btn)
        self.click_on_a_element(RegisterPageLocators.logout_locator)

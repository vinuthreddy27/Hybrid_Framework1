from DemoWebShop.lib.library import Base

class RegisterPageLocators(Base):
    register_link_locater = ("xpath", "//a[.='Register']")
    male_radio_btn = ("id", "gender-male")
    female_radio_btn = ("id", "gender-female")
    first_name_locator = ("id", "FirstName")
    last_name_locator = ("id", "LastName")
    email_locater = ("id", "Email")
    password_locator = ("id", "Password")
    conform_password_locator = ("id", "ConfirmPassword")
    register_btn = ("id", "register-button")
    continue_btn = ("xpath", "//input[@value='Continue']")
    logout_locator = ("xpath", "//li[.='Log out']")

class LoginPageLocators(Base):
    login_link_locator=("xpath","//a[.='Log in']")
    email_locator=("id","Email")
    password_locator=("id","Password")
    login_btn=("xpath","//input[@value='Log in']")
    logout_locator=("xpath","//li[.='Log out']")

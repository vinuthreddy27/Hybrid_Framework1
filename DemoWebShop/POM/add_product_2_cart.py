from DemoWebShop.lib.library import Base
from time import sleep

class Add_2_cart(Base):
    login_link_locator = ("xpath", "//a[.='Log in']")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
    books_locator=("xpath","//ul[@class='top-menu']/./..//a[@href='/books']")
    add_cart_locator=("xpath","//a[.='Computing and Internet']/../..//input[@value='Add to cart']")
    shopping_cart_locator=("xpath","//span[.='Shopping cart']")
    logout_locator=("xpath","//li[.='Log out']")

    def add_2_cart(self,email,password):
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator, email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.click_on_a_element(self.books_locator)
        self.click_on_a_element(self.add_cart_locator)
        self.click_on_a_element(self.shopping_cart_locator)
        self.click_on_a_element(self.logout_locator)

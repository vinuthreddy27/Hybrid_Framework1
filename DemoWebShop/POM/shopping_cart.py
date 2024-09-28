from time import sleep
from DemoWebShop.lib.library import Base

class Shopping_cart(Base):
    login_link_locator = ("xpath", "//a[.='Log in']")
    email_locator = ("id", "Email")
    password_locator = ("id", "Password")
    login_btn = ("xpath", "//input[@value='Log in']")
    shoe_locotor = ("xpath", "//ul[@class='top-menu']/.//a[@href='/apparel-shoes']")
    product_locator=("xpath","(//div[@class='item-box']/..//a[@href='/blue-jeans'])[2]")
    add_cart_btn=("id","add-to-cart-button-36")
    shopping_cart_locator=("xpath","//a[@class='ico-cart']/.//span[.='Shopping cart']")
    quantity_locator=("xpath","//input[@class='qty-input']")
    remove_cart_locator=("xpath","//td[@class='remove-from-cart']")
    update_cart_locator=("name","updatecart")
    logout_locator=("xpath","//li[.='Log out']")

    def shopping_cart(self,email,password,text):
        self.click_on_a_element(self.login_link_locator)
        self.send_keys_to_text_field(self.email_locator,email)
        self.send_keys_to_text_field(self.password_locator, password)
        self.click_on_a_element(self.login_btn)
        self.click_on_a_element(self.shoe_locotor)
        self.click_on_a_element(self.product_locator)
        self.click_on_a_element(self.add_cart_btn)
        self.click_on_a_element(self.shopping_cart_locator)
        self.clear_on_a_element(self.quantity_locator)
        self.send_keys_to_text_field(self.quantity_locator,text)
        self.click_on_a_element(self.remove_cart_locator)
        sleep(1)
        self.click_on_a_element(self.update_cart_locator)
        self.click_on_a_element(self.logout_locator)







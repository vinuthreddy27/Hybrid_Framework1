import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self,driver,ActionChains):
        self.driver=driver
        self.actions = ActionChains(self.driver)

    def wait_for_visibility(self,locator,timeout):
        wait=WebDriverWait(self.driver,timeout)
        condition=visibility_of_element_located(locator)
        element=wait.until(condition)
        return element

    def generate_random_email(self):
        timestamp = time.ctime().split()[3]
        timestamp1 = timestamp.replace(":", "")
        return "vinuth" + timestamp1 + "@gmail.com"

    def search_for_an_element(self,locator):
        element=self.driver.find_element(*locator)
        return element

    def click_on_a_element(self,locator):
        element=self.search_for_an_element(locator)
        element.click()

    def clear_on_a_element(self, locator):
        element = self.search_for_an_element(locator)
        element.clear()

    def send_keys_to_text_field(self,locator,text):
        element=self.search_for_an_element(locator)
        element.send_keys(text)

    def double_click_on_a_element(self,locator):
        element=self.search_for_an_element(locator)
        self.actions.double_click(element).perform()

    def hover_on_a_element(self,locator):
        element=self.search_for_an_element(locator)
        self.actions.move_to_element(element).perform()

    def select_a_option(self,locator1, locator2):
        select_element = self.search_for_an_element(locator1)
        s1 = Select(select_element)
        element=self.search_for_an_element(locator2)
        s1.select_by_visible_text(element.text)

    def select_a_option2(self,locator1, locator2):
        select_element = self.search_for_an_element(locator1)
        s1 = Select(select_element)
        element=self.search_for_an_element(locator2)
        s1.select_by_value(element.text)

    def select_a_option3(self, locator1, locator2):
        select_element = self.search_for_an_element(locator1)
        s1 = Select(select_element)
        element = self.search_for_an_element(locator2)
        s1.select_by_index(element.text)

    def dismiss_an_alert(self):
        self.driver.switch_to.alert.dismiss()

    def accept_an_alert(self):
        self.driver.switch_to.alert.accept()

    def send_keys_to_alert(self,text):
        self.driver.switch_to.alert.send_keys(text)

    def navigational_commands(self):
        self.driver.back()

    def navigational_command_refresh(self):
        self.driver.refresh()

    def navigational_command_forward(self):
        self.driver.forward()


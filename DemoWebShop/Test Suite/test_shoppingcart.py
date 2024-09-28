from selenium.webdriver import ActionChains
from DemoWebShop.POM.add_product_2_cart import Add_2_cart

def  test_add_2_cart(driver):
      ad_2_cart_page_obj=Add_2_cart(driver,ActionChains)
      ad_2_cart_page_obj.add_2_cart("reddyvinuth27@gmail.com","selenium")

      assert driver.find_element("xpath", "//div[@class='topic-html-content-title']").is_displayed()




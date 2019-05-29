from selenium import webdriver
import time
import unittest

class Login_ZenTao_Test():
    def __init__(self,driver):
        self.driver=driver

    def login(self,user,password):
         self.driver.find_element_by_id("account").send_keys(user)
         self.driver.find_element_by_xpath('.//*[@name="password"]').send_keys(password)
         self.driver.find_element_by_xpath('.//*[@id="submit"]').click()

    def is_login_success(self):
          try:
              time.sleep(5)
              t=self.driver.find_element_by_xpath(".//*[@id='userMenu']/a").text
              print(t)
              return t
          except:
              return ""

    def is_alter_exit(self):
            try:
                    time.sleep(3)
                    alter=self.driver.switch_to.alert
                    text=alter.text
                    alter.accept()
                    return text

            except:
                   pass

if __name__ == '__main__':
    unittest.main()
    # driver=webdriver.Firefox()
    # driver.get("http://47.104.190.48:8088/zentao/user-login.html")
    # login_zento=Login_ZenTao_Test(driver)
    # login_zento.login("test123","!@123456")

#coding:utf-8
from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def setUp(self):
        # self.driver=webdriver.Firefox()
        self.driver.get("http://47.104.190.48:8088/zentao/user-login.html")



    def tearDown(self):
            self.driver.delete_all_cookies()
            self.driver.refresh()
            self.is_alter_exit()
            # self.driver.quit()
    @classmethod
    def tearDownClass(cls):
           cls.driver.quit()

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


    def test_01(self):
            '''测试用例11111111111111111111111111111111'''
            time.sleep(2)
            self.login("test123","!@123456")
            d=self.is_login_success()
            print(d)
            self.assertTrue(d=="test123")



    def test_02(self):
            '''执行用例2222222222222222222222'''
            # self.driver=webdriver.Firefox()
            # self.driver.get("http://47.104.190.48:8088/zentao/user-login.html")
            time.sleep(2)
            self.login("test124","33333")
            time.sleep(3)
            t=self.is_login_success()
            print("获取结果：%s"%t)
            self.assertTrue(t=="13333")





#coding:utf-8
from selenium import webdriver
import time
import unittest
from lianxi.login_zentao import Login_ZenTao_Test

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.zentao=Login_ZenTao_Test(cls.driver)

    def setUp(self):
        # self.driver=webdriver.Firefox()
        self.driver.get("http://47.104.190.48:8088/zentao/user-login.html")

    def tearDown(self):
            self.driver.delete_all_cookies()
            self.driver.refresh()
            self.zentao.is_alter_exit()
            # self.driver.quit()
    @classmethod
    def tearDownClass(cls):
           cls.driver.quit()


    def test_01(self):
            '''测试用例11111111111111111111111111111111'''
            time.sleep(2)
            self.zentao.login("test123","!@123456")
            d=self.zentao.is_login_success()
            print(d)
            self.assertTrue(d=="test123")



    def test_02(self):
            '''执行用例2222222222222222222222'''
            # self.driver=webdriver.Firefox()
            # self.driver.get("http://47.104.190.48:8088/zentao/user-login.html")
            time.sleep(2)
            self.zentao.login("test123","133333")
            time.sleep(3)
            t=self.zentao.is_login_success()
            print("登录失败，获取结果：%s"%t)
            self.assertTrue(t=="")





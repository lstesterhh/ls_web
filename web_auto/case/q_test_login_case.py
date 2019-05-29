from selenium import webdriver
import unittest
from page.zentao_login_page import LoginPage,login_url
'''
1、输入test123,输入！@123456 点击登录
2、输入test123,输入空的密码，点击登录
3、输入test23，输入！@123456 点击记住用户名 点击登录
4、点击忘记密码
'''
class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginp=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alert_exit()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        self.loginp.input_user("test123")
        self.loginp.input_password("!@123456")
        self.loginp.click_login_buttton()
        result=self.loginp.get_login_name()
        print(result)
        self.assertTrue(result == "test123")

    def test_02(self):
        self.loginp.input_user("test123")
        self.loginp.click_login_buttton()
        result=self.loginp.get_login_name()
        print(result)
        self.assertTrue(result == None)

    def test_03(self):
        self.loginp.input_user("test123")
        self.loginp.input_password("!@123456")
        self.loginp.click_keep_login()
        self.loginp.click_login_buttton()
        result=self.loginp.get_login_name()
        print(result)
        self.assertEqual(result,"test123")

    def test_04(self):
        self.loginp.click_forget_password()
        result=self.loginp.is_refrash_exit()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
  unittest.main()
from selenium import webdriver
import unittest
from page.zentao_login_page import LoginPage,login_url
import ddt
import os
from common.read_excel import ExcelUtil
'''
1、输入test123,输入！@123456 点击登录
2、输入test123,输入空的密码，点击登录
3、输入admin，输入！@123456 点击记住用户名 点击登录
'''
testdatas=[
    {"user": "test123", "psw": "!@123456", "expect": True},
    {"user": "test123", "psw": "", "expect": False},
    {"user": "admin", "psw": "!@123456", "expect": False},
]
# projectpath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# filepath=os.path.join(projectpath,"common","dates.xls")
# print(filepath)
# datas = ExcelUtil(filepath)
# testdatas=datas.dict_data()
# print(testdatas)

@ddt.ddt
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        self.loginp.is_alert_exit()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def login_case(self, user, psw, expect):
        self.loginp.input_user(user)
        self.loginp.input_password(psw)
        self.loginp.click_login_buttton()
        result=self.loginp.get_result_name(user)
        print("测试结果：%s" % result)
        self.assertEqual(result,expect)

    @ddt.data(*testdatas)
    def test_01(self,data):
        print("测试数据:%s" % data)
        self.login_case(data["user"], data["psw"], data["expect"])

    #  def test_01(self):
    #     data01 = testdatas[0]
    #     print("测试数据:%s" % data01)
    #     self.login_case(data01["user"], data01["psw"], data01["expect"])

    # def test_02(self):
    #     data02 = testdatas[1]
    #     print("测试数据%s" % data02)
    #     self.login_case(data02["user"], data02["psw"], data02["expect"])
    #
    # def test_03(self):
    #     data03 = testdatas[2]
    #     print("测试数据%s" % data03)
    #     self.login_case(data03["user"], data03["psw"], data03["expect"])
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
  unittest.main()
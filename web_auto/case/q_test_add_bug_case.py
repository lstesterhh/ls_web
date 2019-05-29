import unittest
from selenium import webdriver
import time
from page.zentao_login_page import LoginPage
from page.zentao_addbug_page import AddBugPage

my_url="http://47.104.190.48:8088/zentao/my/"
class AddBugCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        login=LoginPage(cls.driver)
        login.login()
        cls.addbug=AddBugPage(cls.driver)

    def setUp(self):
        self.driver.get(my_url)

    def test_add_bug(self):
        timestr=time.strftime("%Y_%m_%d_%H_%M_%S")
        self.addbug.add_bug(timestr)
        result=self.addbug.title_list()
        print(result)
        assert result =="测试标题: " + timestr

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
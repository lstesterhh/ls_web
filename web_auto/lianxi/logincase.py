from lianxi.loginFuc import login
import unittest
from selenium import webdriver

class TestCase(unittest.TestCase):

      def setUp(self):
          self.driver=webdriver.Firefox()
          self.driver.get("http://47.104.190.48:8088/zentao/user-login.html")
      def testcase_01(self):
          login(self.driver,"test123","!@123456")
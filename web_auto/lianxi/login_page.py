from lianxi.base import Base
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By

class LoginPage(Base):

   # loc1=(By.ID,"account")
   # loc2=(By.NAME,"password")
   # loc3=(By.ID,"submit")
   loc1=("id","account")
   loc2=("name","password")
   loc3=("id","submit")

   def login(self):
        self.send(self.loc1,"test123")
        self.send(self.loc2,"!@123456")
        self.click(self.loc3)


if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://47.104.190.48:8088/zentao/user-login.html")
    lp=LoginPage(driver)
    lp.login()




#coding:utf-8
from selenium import webdriver
from common.base import Base
import unittest
login_url="http://47.104.190.48:8088/zentao"
class LoginPage(Base):
    loc_user=("id","account")
    loc_psw=("name","password")
    loc_submit=("id","submit")
    loc_keep_login=("xpath",".//*[@id='keeplogin']/label")
    loc_forget=("link text","忘记密码")
    loc_success=("xpath",".//*[@id='userMenu']/a")
    loc_refrash=("link text","刷新")

    def input_user(self,text):
        self.send(self.loc_user,text)

    def input_password(self,text):
        self.send(self.loc_psw,text)

    def click_login_buttton(self):
        self.click(self.loc_submit)

    def click_keep_login(self):
        self.click(self.loc_keep_login)

    def click_forget_password(self):
        self.click(self.loc_forget)

    def login(self,user="test123",psw="!@123456",keep_login=False):
        self.driver.get(login_url)
        self.input_user(user)
        self.input_password(psw)
        if keep_login:self.click_keep_login()
        self.click_login_buttton()

    def get_login_name(self):
        try:
           loginuser= self.get_text(self.loc_success)
           return loginuser
        except:
            return ""

    def get_result_name(self,user):
        result=self.text_in_element(self.loc_success,user)
        return result


    def is_alert_exit(self):
        a=self.is_alert()
        if a:
            a.accept()

    def is_refrash_exit(self):
        result=self.is_element_exist(self.loc_refrash)
        return result


if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get(login_url)
    loginpage=LoginPage(driver)
    # loginpage.input_user("test123")
    # loginpage.input_password("")
    # # loginpage.click_keep_login()
    # loginpage.click_login_buttton()
    # name=loginpage.get_login_name()
    # print(name)
    loginpage.login()





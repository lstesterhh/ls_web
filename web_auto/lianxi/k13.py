from selenium import webdriver
from lianxi.base import Base

driver=webdriver.Firefox()
driver.get("http://47.104.190.48:8088/zentao/user-login.html")
# loc1=("xpath",".//*[text()='忘记密码']")
# zentao=Base(driver)
# r1=zentao.is_title("用户登录 - 禅道")
# print(r1)
#
# r2=zentao.is_title_contains("禅道")
# print(r2)
#
# r3=zentao.is_text_in_element(loc1,"忘记密码")
# print(r3)
#
# r4=zentao.is_text_in_element(loc1,"****")
# print(r4)

loc1=("xpath",".//*[@id='account']")
loc2=("xpath",".//*[@name='password']")
loc3=("id","submit")

zentao=Base(driver)
zentao.sendkeys(loc1,"test123")
zentao.sendkeys(loc2,"3333")
zentao.click(loc3)
r=zentao.is_alert_present()
print(r)
print(r.text)
r.accept()


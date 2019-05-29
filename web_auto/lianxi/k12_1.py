#coding:utf-8
from lianxi.base import Base
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://47.104.190.48:8088/zentao/user-login.html")

zentao=Base(driver)

loc1=("id","account")
r1=zentao.findelement(loc1)
r2=r1.is_displayed()
print(r2)

loc2=("id","hiddenwin")
r3=zentao.findelement(loc2)
r4=r3.is_displayed()
print(r4)



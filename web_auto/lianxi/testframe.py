#coding:utf-8
from selenium import webdriver
import time
from page.zentao_login_page import LoginPage
from pykeyboard import PyKeyboard
from pymouse import PyMouse
driver=webdriver.Firefox()
a=LoginPage(driver)
a.login()
driver.get("http://47.104.190.48:8088/zentao/bug-create-1-0-moduleID=0.html")
time.sleep(2)
driver.find_element_by_xpath(".//*[@title='图片']/span").click()
time.sleep(2)
driver.find_element_by_css_selector(".ke-inline-block.ke-upload-button").click()
time.sleep(2)
k=PyKeyboard()
s="D:\A.png"
for i in s:
    k.tap_key(i)
time.sleep(2)
k.tap_key(k.enter_key)
driver.find_element_by_xpath(".//*[@title='确定\']/input").click()


# js='document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML=("SFSDFSDFSDFSDF")'
# driver.execute_script(js)
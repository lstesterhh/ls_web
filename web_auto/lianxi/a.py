# def testFun():
#     temp = [lambda x : i*x for i in range(4)]
#     return temp
#
# for everyLambda in testFun():
#     print (everyLambda(2))
from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
js="document.getElementById('kw').value='selenium';"
driver.execute_script(js)
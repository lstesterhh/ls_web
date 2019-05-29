from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By


'''
        Example:
            from selenium.webdriver.support.ui import WebDriverWait \n
            element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("someId")) \n
            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).\ \n
                        until_not(lambda x: x.find_element_by_id("someId").is_displayed())

'''
driver=webdriver.Firefox()
driver.get("http://47.104.190.48:8088/zentao/user-login.html")
def find_element(driver,locator,timeout=10,t=0.5):
        e_user=WebDriverWait(driver, timeout,t).until(lambda x: x.find_element(*locator))
        return e_user


loc1=(By.ID,"account")
loc2=(By.NAME,"password")
loc3=(By.ID,"submit")

find_element(driver,loc1).send_keys("test123")
find_element(driver,loc2).send_keys("!@123456")
find_element(driver,loc3).click()





# e_user=WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("account"))
# print(e_user)
# e_user.send_keys("test123")
# e_pswr=WebDriverWait(driver, 10).until(lambda x: x.find_element_by_name("password"))
# print(e_pswr)
# e_pswr.send_keys("!@123456")
# e_submit=WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("submit"))
# e_submit.click()

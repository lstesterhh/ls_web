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
        e_user=WebDriverWait(driver,timeout,t).until(lambda x: x.find_element(*locator))
        return e_user


loc1=(By.ID,"account")
r1=driver.find_element(driver,loc1).send_keys("1111")
print(r1)

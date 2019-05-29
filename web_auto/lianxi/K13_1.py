from selenium import webdriver
from lianxi.base import Base
from selenium.webdriver.support import expected_conditions

driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")

loc1=("id","su")
zen=Base(driver)
r1=zen.is_value_in_element(loc1,"百度一下")
print(r1)


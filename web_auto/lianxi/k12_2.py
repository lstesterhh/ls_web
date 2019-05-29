#coding:utf-8
from lianxi.base import Base
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
zentao=Base(driver)
loc1=("link text","设置")
a=zentao.findelement(loc1)
ActionChains(driver).move_to_element(a).perform()

loc2=("link text","搜索设置")
zentao.click(loc2)


#没有被选中
loc3=("xpath",".//*[@id='nr']/option[3]")
r1=zentao.findelement(loc3)
r2=r1.is_selected()
print(r2)

loc4=("id","nr")
select=zentao.findelement(loc4)
a2=Select(select).select_by_index(2)

#被选中了 true
r3=zentao.findelement(loc3).is_selected()
print(r3)

#元素没找到---报错timeout
loc5=("id","***")
select=zentao.findelement(loc4)
a2=Select(select).select_by_index(2)

r4=zentao.findelement(loc5).is_selected()
print(r4)
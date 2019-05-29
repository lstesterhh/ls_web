from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("http://www.bigbang.wiki/#/main")

driver.find_element_by_xpath(".//*[@id='app']/div[1]/div/div[2]/div[2]/ul/li[1]").click()
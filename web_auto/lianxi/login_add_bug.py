from lianxi.base import Base
import time
from selenium.webdriver.support.select import Select
from selenium import webdriver

class AddBug(Base):
   loc1_test=("xpath",".//*[@data-id='qa']/a")
   loc2_bug=("xpath",".//*[@class='active']/a")
   loc3_tibug=("xpath",".//*[@id='createActionMenu']/a")
   loc4_mokuai=("xpath",".//*[@id='module_chosen']/a")
   loc5_denglu=("xpath",".//*[@id='module_chosen']/div/ul/li[1]")
   loc6_yingxiang=("xpath",".//*[@id='openedBuild_chosen']/ul")
   loc7_zhugan=("xpath",".//*[@id='openedBuild_chosen']/div/ul/li[1]")
   loc8_biaoti=("css selector","#title")
   iframe=("class name","ke-edit-iframe")
   body=("xpath",".//*[@class='article-content']/p")
   save=("xpath",".//*[@id='submit']")
   titlelist=("xpath",".//*[@id='bugList']/tbody/tr/td[4]/a")

   def add_bug(self,timestr):
       self.click(self.loc1_test)
       self.click(self.loc2_bug)
       self.click(self.loc3_tibug)
       self.click(self.loc4_mokuai)
       self.click(self.loc5_denglu)
       self.click(self.loc6_yingxiang)
       self.click(self.loc7_zhugan)
       self.send(self.loc8_biaoti,"测试标题: " + timestr)
       frame=self.find(self.iframe)
       self.driver.switch_to_frame(frame)
       self.send(self.body,"测试正文")
       self.driver.switch_to_default_content()
       self.click(self.save)

   def title_list(self):
       all_title=self.finds(self.titlelist)
       try:
           t1=all_title[0].text
           print(t1)
           return t1
       except:
           return []

if __name__ == '__main__':
    driver=webdriver.Firefox()
    driver.get("http://47.104.190.48:8088/zentao/user-login.html")
    from lianxi.login_page import LoginPage
    login=LoginPage(driver)
    login.login()

    addbug=AddBug(driver)
    timestr=str(time.time())
    addbug.add_bug(timestr)

    result=addbug.title_list()
    print(result)
    assert result =="测试标题: " + timestr




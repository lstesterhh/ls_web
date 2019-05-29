from selenium import webdriver
from time import sleep
from pykeyboard import PyKeyboard
from pymouse import PyMouse

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', 'd:\\')
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('http://note.youdao.com/')
driver.find_element_by_xpath(".//*[@id='btn-down']").click()
sleep(3)

# 默认在取消按钮上，先切换到保存文件上
k = PyKeyboard()

# 模拟Tab
k.tap_key(k.tab_key)
sleep(3)
# 发送Enter回车
k.tap_key(k.enter_key)


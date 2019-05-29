#coding:utf-8
import unittest
from common import HTMLTestRunner


start_dir="D:\\web_auto\\case"
discover=unittest.defaultTestLoader.discover(start_dir=start_dir,pattern="test*.py")
print(discover)

reportpath="D:\\web_auto\\report\\"+"report.html"
fp=open(reportpath,"wb")
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"报告标题",description=u"报告内容描述",retry=1)

runner.run(discover)
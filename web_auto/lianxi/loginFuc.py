import unittest

def login(driver,user,password):
     driver.find_element_by_id("account").send_keys(user)
     driver.find_element_by_xpath('.//*[@name="password"]').send_keys(password)
     driver.find_element_by_xpath('.//*[@id="submit"]').click()
if __name__ == '__main__':
   unittest.main()
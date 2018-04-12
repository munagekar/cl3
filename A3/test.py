from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import time

driver = webdriver.Firefox()
for i in range(100):
  
  n1=randint(0,1023)
  n2=randint(0,1023)
  
  
  
  
  driver.get("http://localhost:1234")
  t1 = driver.find_element_by_name('t1')
  t2 = driver.find_element_by_name('t2')
  t1.send_keys(str(n1))
  t2.send_keys(str(n2))
  t1.send_keys(Keys.RETURN)
  time.sleep(1)
  assert ("Anwer is "+str(n1*n2) in driver.page_source),'Mismatch'
  

driver.close()

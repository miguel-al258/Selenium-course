from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
t=4


driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://unadmexico.mx/")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.close()
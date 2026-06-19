from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
t=.7


driver.get("https://letcode.in/radio")
driver.maximize_window()
#driver.find_element(By.XPATH, "//button[@id='modern']").click()
time.sleep(t)
btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='no']")))
btn1.click()
btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='one']")))
btn2.click()
btn2_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='two'] ")))
btn2_2.click()

driver.close()
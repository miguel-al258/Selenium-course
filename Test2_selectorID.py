from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
t=2


driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

nom = driver.find_element(By.ID, "userName")
nom.send_keys("Miguel")
time.sleep(t)
driver.find_element(By.ID, "userEmail").send_keys("miguel@gmail.com")
time.sleep(t)
driver.find_element(By.ID,"currentAddress").send_keys("Calle1")
time.sleep(t)
driver.find_element(By.ID, "permanentAddress").send_keys("Calle2")
time.sleep(t)
driver.execute_script("window.scrollTo(0,300)")
driver.find_element(By.ID, "submit").click()
time.sleep(t)


driver.close()
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
t=2


driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

nom = driver.find_element(By.XPATH, "//input[@id='userName']")
nom.send_keys("Miguel")
time.sleep(t)
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("miguel@gmail.com")
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Calle1")
time.sleep(t)
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Calle2")
time.sleep(t)
driver.execute_script("window.scrollTo(0,300)")
driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(t)


driver.close()
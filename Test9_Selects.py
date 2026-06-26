from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
t=1


driver.get("https://letcode.in/dropdowns")
driver.maximize_window()
time.sleep(t)
fruits = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='fruits']")))
fruitSelect = driver.find_element(By.XPATH,"//select[@id='fruits']")
ft = Select(fruitSelect)
ft.select_by_visible_text("Apple")
time.sleep(t)
ft.select_by_index(2)
time.sleep(t)
ft.select_by_value("3")
time.sleep(t)

heroes = Select(driver.find_element(By.ID, "superheros" ))
heroes.select_by_index(0)
time.sleep(t)
heroes.select_by_index(3)
time.sleep(t)
heroes.select_by_index(7)
time.sleep(t)


driver.close()
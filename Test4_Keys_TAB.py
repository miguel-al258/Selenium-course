from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
t=2


driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

nom = driver.find_element(By.CSS_SELECTOR, "#userName")
nom.send_keys("Miguel")
nom.send_keys(Keys.TAB + "miguel@gmail.com" + Keys.TAB + "Calle1" + Keys.TAB + "Calle2" + Keys.TAB + Keys.ENTER )
time.sleep(t)



driver.close()
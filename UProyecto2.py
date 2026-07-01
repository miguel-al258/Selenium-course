from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://letcode.in/forms")
driver.maximize_window()
t=2

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='grippy-host']")))
element.click()
driver.find_element(By.XPATH, "//input[@id='firstname']").send_keys("Miguel"+ Keys.TAB +"Lopez"+ Keys.TAB+"miguel@gotmail.com")
time.sleep(t)
country_code = Select(driver.find_element(By.XPATH,"//select[@class='flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background focus:outline-none focus:ring-2 focus:ring-emerald-500/20 focus:border-emerald-500 transition-all duration-200']"))
country_code.select_by_value("52")
driver.find_element(By.XPATH,"//input[@id='Phno']").send_keys("7223212320"+ Keys.TAB + "Calle1" + Keys.TAB + "Calle2" + Keys.TAB + "Mexico" + Keys.TAB + "55220"+ Keys.TAB + "Mexico")
driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)
driver.find_element(By.XPATH, "//input[@id='Date']").send_keys("11102018")
time.sleep(t)
driver.find_element(By.XPATH,"//input[@id='male']").click()
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
time.sleep(t)
submit = driver.find_element(By.XPATH, "//input[@value='Submit']")
submit.click()
time.sleep(5)
driver.close()
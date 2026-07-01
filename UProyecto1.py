from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
t = 2
t2 = 5

driver.get("https://testpages.eviltester.com/pages/forms/text-inputs/")
driver.maximize_window()
time.sleep(t)

try:
    text = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='text-input']")))
    text = driver.find_element(By.XPATH, "//input[@id='text-input']")
    text.send_keys("Miguel")
    search = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='search-input']")))
    search = driver.find_element(By.XPATH, "//input[@id='search-input']")
    search.send_keys("Lopez")
    pw = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password-input']")))
    #pw = driver.find_element(By.XPATH,"//input[@id='password-input']").send_keys("mike123")
    email = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='email-input']")))
    email = driver.find_element(By.XPATH,"//input[@id='email-input']").send_keys("miguel@gmail.com")
    url = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='url-input']")))
    url = driver.find_element(By.XPATH,"//input[@id='url-input']").send_keys("https://testpages.eviltester.com/pages/forms/text-inputs/")
    tel = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='tel-input']")))
    tel = driver.find_element(By.XPATH,"//input[@id='tel-input']").send_keys(7223212742)
    btn_sub = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//input[@value='submit']")))
    ir = driver.execute_script("arguments[0].scrollIntoView();", btn_sub)
    btn_sub = driver.find_element(By.XPATH, "//input[@value='submit']").click()
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(t2)

except TimeoutException as ex:
    
    print("Elemento no disponible")

driver.get("https://testpages.eviltester.com/pages/forms/other-text/")

try:
    textA =  WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@id='text-area-input']")))
    textA = driver.find_element(By.XPATH, "//textarea[@id='text-area-input']").send_keys("A string for typing, or setting form fields. For setting file inputs, this could be a local file path")
    mult_sel = Select(driver.find_element(By.ID,"multi-select-input"))
    mult_sel.select_by_index(0)
    mult_sel.select_by_index(1)
    time.sleep(t)
    selec = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='select-input']")))
    selec = Select(driver.find_element(By.XPATH,"//select[@id='select-input']"))
    selec.select_by_value("dd1")
    time.sleep(t)
    selec.select_by_value("dd3")
    time.sleep(t)
    btn_sub = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,"//input[@value='submit']")))
    ir = driver.execute_script("arguments[0].scrollIntoView();", btn_sub)
    btn_sub = driver.find_element(By.XPATH, "//input[@value='submit']").click()
    time.sleep(t2)
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(t2)
    
except TimeoutException as ex:
    
    print("Elemento no disponible")
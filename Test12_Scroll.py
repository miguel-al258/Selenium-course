from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome()
t=3


driver.get("https://pixabay.com/photos/")
driver.maximize_window()
time.sleep(t)
#driver.execute_script("window.scrollTo(0,300)")

try:
    cookie = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon']")))
    cookie.click()
    print("Se cierra ventana de cookies")
    time.sleep(t)
    buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='button--af32y tonal--Q6v69 light--yqIMf center--aZtxo responsive__r_2s_1']")))
    ir = driver.execute_script("arguments[0].scrollIntoView();", buscar)
    buscar = driver.find_element(By.XPATH,"//a[@class='button--af32y tonal--Q6v69 light--yqIMf center--aZtxo responsive__r_2s_']")
    buscar.click()
    
    time.sleep(t)


except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")



driver.close()
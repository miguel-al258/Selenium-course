from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome()
t=1


driver.get("https://testpages.eviltester.com/pages/files/file-upload/")
driver.maximize_window()
time.sleep(t)
driver.execute_script("window.scrollTo(0,300)")

try:
    
    choose_file = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "fileinput")))
    choose_file = driver.find_element(By.ID,"fileinput")
    print("Enviando archivo al elemento input")
    choose_file.send_keys(r"C:\Users\MIGUEL ANGEL LOPEZ\Documents\Selenium\Imagenes\demo1.jpg")
    time.sleep(t)
    print("Click en checkbox image")
    choose_file = driver.find_element(By.ID, "itsanimage").click()
    time.sleep(t)
    print("Click en boton Uploaded")
    upload_btn = driver.find_element(By.NAME,"upload").click()
    time.sleep(t)


except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")



driver.close()
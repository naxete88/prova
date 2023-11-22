from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

svc = webdriver.ChromeService(executable_path = binary_path)
driver = webdriver.Chrome(service=svc)
driver.get('https://www.gmail.com')

usuario = driver.find_element(By.ID,"identifierId")
usuario.send_keys('imbernad88@gmail.com')
usuario.send_keys(Keys.ENTER)
time.sleep(6)
clave = driver.find_element(By.NAME,"password")
clave.send_keys("tupasswordpersonal")
clave.send_keys(Keys.ENTER)
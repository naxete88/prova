import unittest
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

svc = webdriver.ChromeService(executable_path = binary_path)

driver = webdriver.Chrome(service=svc)
driver.get("https://www.w3schools.com/html/html_tables.asp")
time.sleep(3)
permiso = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/div[1]/div[2]")
permiso.click()
time.sleep(3)

valor = driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr[2]/td[2]").text
print(valor)

#que nos diga el numero de filas y columnas
rows = len(driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr"))
columns = len(driver.find_elements(By.XPATH,"//*[@id='customers']/tbody/tr[1]/th"))

print(rows)
print(columns)

for n in range(2, rows+1):
    for b in range(1, columns+1):
        dato = driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
        print(dato, end='      ')
    print()

driver.close()

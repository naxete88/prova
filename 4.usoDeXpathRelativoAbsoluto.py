# si no encontramos un elemento por ID, NAME
import unittest
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

svc = webdriver.ChromeService(executable_path = binary_path)

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=svc)

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("https://www.google.es")
        permiso = driver.find_element(By.ID,"L2AGLb")
        permiso.send_keys(Keys.ENTER)
        time.sleep(3)
        buscar_por_xpath = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
        buscar_por_xpath.send_keys("selenium",Keys.ARROW_DOWN)
        time.sleep(20)
        buscar_por_xpath

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()

# Xpath es una estructura de objetos, similar al DISCO C, es una estructura XML.
# para buscar en google, inspeccionar, sources.
# para encontrar Xpath, inspeccionar, click derecho, copy y copyXpath.
# Xpath relativo: parte de un nodo especifico. Cada nodo seria lo que hay entre \\ en 
# una busqueda de C.
# Xpath absoluto: toda la ruta.
# Arrow Down da tecla hacia abajo. 

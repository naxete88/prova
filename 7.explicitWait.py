import unittest
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

svc = webdriver.ChromeService(executable_path = binary_path)

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=svc)

    def test_usando_Explicit_wait(self):
        driver = self.driver
        driver.get("https://www.google.es")
        # esperamos a que cargue el objeto, hacemos 10 intentos
        try:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.NAME, "q"))
            )
        finally:
            driver.quit()
        
if __name__ == '__main__':
    unittest.main()

# Explicit wait trata de dar condiciones para cargar ciertos componentes
# en un script. Que no inicie automatizacion hasta encontrar un elemento.
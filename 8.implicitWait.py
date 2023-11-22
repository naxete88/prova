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

    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) # segundos
        driver.get("https://www.google.es")
        # componente dinamico, aquel que cambia su id o nombre de cuando
        # se carga a cuando se usa.
        myDynamicElement = driver.find_element(By.NAME,"q")

if __name__ == '__main__':
    unittest.main()

# implicit wait: espera una sentencia en especifico que nosotros 
# le estamos diciendo.
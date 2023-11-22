import unittest
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

svc = webdriver.ChromeService(executable_path = binary_path)

class usandoUnitTest(unittest.TestCase):
# para iniciar el driver
    def setUp(self):
        self.driver = webdriver.Chrome(service=svc)

    def test_buscar(self):
        driver = self.driver
        driver.get('http://www.google.es')
        self.assertIn("Google", driver.title)
        # verifica que la palabra google este en el titulo
        permiso = driver.find_element(By.ID,"L2AGLb")
        permiso.send_keys(Keys.ENTER)
        elemento = driver.find_element(By.NAME,"q")
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elemento" not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
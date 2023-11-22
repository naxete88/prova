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

    def test_usando_pagina_siguiente(self):
        driver = self.driver
        driver.get("https://www.gmail.com")
        time.sleep(3)
        driver.get("https://www.google.es")
        time.sleep(3)
        driver.get("https://www.youtube.com")
        #para regresar a la pagina anterior
        driver.back()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        # para avanzar
        driver.forward()
        time.sleep(3)

    def tearDown(self):
         self.driver.close()

if __name__ == '__main__':
    unittest.main()
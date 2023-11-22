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

    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get('https://www.google.es')
        time.sleep(5)
        # abrir una nueva ventana
        driver.execute_script("window.open('');")
        time.sleep(5)
        # posicionar en la pestana 1
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://stackoverflow.com')
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
    
    def tearDown(self):
         self.driver.close()

if __name__ == '__main__':
    unittest.main()
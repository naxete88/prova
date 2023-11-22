# toggle es un switch para validar una informacion (boton de on off)
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

    def test_usando_toggle(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
        time.sleep(3)
        permiso = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/div[1]/div[2]")
        permiso.click()
        time.sleep(3)
        toggle = driver.find_element(By.XPATH,"/html/body/div[5]/div[1]/div[1]/label[3]/div")
        toggle.click()
        time.sleep(3)
        toggle.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close


if __name__ == '__main__':
    unittest.main()

    

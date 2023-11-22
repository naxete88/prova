from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

svc = webdriver.ChromeService(executable_path = binary_path)

class usando_unittest(unittest.TestCase):

    def setUp(self):
        chromeOptions = Options()
        chromeOptions.add_experimental_option("prefs", 
                                              {"download.default_directory" : "C:\",
                                               }
        )
        self.driver = webdriver.Chrome(service=svc, chrome_options = chromeOptions)

    def test_descargando_archivos(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/tags/att_a_download.asp")
        time.sleep(3)
        permiso = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div[3]/div[1]/div[2]")
        permiso.click()
        time.sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH))
        
if __name__ == '__main__':
    unittest.main()
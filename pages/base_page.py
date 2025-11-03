from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class BasePage:
    def __init__(self, driver = 'chrome'):
        options = Options()
        options.add_argument('--headless=new')
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def quit(self):
        self.driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self,(type, value)):
        return self.wait.until(EC.presence_of_element_located((By.type, value)))

    def quit(self):
        self.driver.quit()

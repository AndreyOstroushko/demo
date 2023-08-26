from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from base.base_class import Base


class MainPage(Base):

    base_url = 'https://demowebshop.tricentis.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''Locators'''
    button_autorization = '//a[@class="ico-login"]'

    '''Get waiting autarization button'''
    def get_autorization_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_autorization)))

    '''Actions'''
    def click_autorization_button(self):
        self.get_autorization_button().click()

    '''Method'''
    def select_autorization(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.click_autorization_button()

import types
import typing
from selenium import webdriver
import Booking.constants as const
import os
from selenium.webdriver.common.by import By

class Booking(webdriver.Chrome):
    def __init__(self,driver_path=os.getcwd(),teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def landing_first_page(self):
        if self.teardown:
            self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def select_currency(self):
        currency_element = self.find_element(By.CSS_SELECTOR,'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()

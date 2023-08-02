import types
import typing
from selenium import webdriver
import Booking.constants as const
import os
from selenium.webdriver.common.by import By

class Booking(webdriver.Edge):
    def __init__(self,driver_path=os.getcwd(),teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def landing_first_page(self):
        """
        Opens the base URL if the teardown flag is set.
        """
        if self.teardown:
            self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Quits the webdriver on exit.
        """
        self.quit()

    def dismiss_signin_popup(self):
        """
        Dismisses the sign-in popup if present.
        """
        try:
            but = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign in information."]')
            but.click()
        except Exception:
            pass

    def select_currency(self,currency=None):
        """
        Opens the currency selection dropdown and selects the desired currency.
        """
        currency_element = self.find_element(By.CSS_SELECTOR,'button[data-testid="header-language-picker-trigger"]')
        currency_element.click()

        if currency:
        # select_currency_element = self.find_element(By.CSS_SELECTOR,f'button[data-testid="selection-item={currency}"]')
            try:
                select_currency_element = self.find_element(By.CLASS_NAME,"ea1163d21f")
                select_currency_element.click()
            except Exception:
                 print(f"Currency '{currency}' not found. Keeping default currency.")
        else:
            print("No currency provided. Keeping default currency.")



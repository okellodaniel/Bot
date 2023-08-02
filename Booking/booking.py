
from selenium import webdriver
import Booking.constants as const
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore, Back, Style

class Booking(webdriver.Edge):
    def __init__(self,driver_path=os.getcwd(),teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        self.implicitly_wait(10)
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
            print(but.get_attribute())
            but.click()
        except Exception as e:
            print(Fore.RED,e)
            pass

    def select_currency(self,currency=None):
        """
        Opens the currency selection dropdown and selects the desired currency.
        """
        currency_element = self.find_element(By.CSS_SELECTOR,'button[data-testid="header-currency-picker-trigger"]')
        actions = ActionChains(self)
        actions.move_to_element(currency_element).click().perform()
        currency_element.click()

        if currency:
            try:
                select_currency_element = self.find_elements(By.CSS_SELECTOR,f'button[data-testid="selection-item"]')
                for i in select_currency_element:
                    select_currency = i.find_element(By.CLASS_NAME,"ea1163d21f")
                    if select_currency.text == f"{currency}":
                        i.click()
            except Exception as e:
                 print(f"Currency '{currency}' not found. Keeping default currency.",e)
        else:
            print("No currency provided. Keeping default currency.")



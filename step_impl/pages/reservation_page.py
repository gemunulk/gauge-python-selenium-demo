from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage
import time


class ReservationPageLocators:
    """A class for Reservation page locators. All login page locators should come here"""
    SIGN_OFF_LINK   = (By.XPATH, "//a[contains(text(),'SIGN-OFF')]")


class ReservationPage(BasePage):
    URL = '{}/mercuryreservation.php'.format(BasePage.MAIN_URL)
    
    """Reservation page actions """
    def visit(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def validate_reservation_page(self):
        assert self.is_displayed(ReservationPageLocators.SIGN_OFF_LINK), "SIGN_OFF_LINK not displayd" 

        

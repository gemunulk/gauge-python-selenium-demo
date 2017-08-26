from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage
import time


class LoginPageLocators:
    """A class for login page locators. All login page locators should come here"""

class LogoutPage(BasePage):
    URL = '{}/mercurysignoff.php'.format(BasePage.MAIN_URL)
    
    """Logout page actions """
    def visit(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        

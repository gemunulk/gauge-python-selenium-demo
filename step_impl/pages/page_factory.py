from getgauge.python import before_suite, after_suite
from selenium import webdriver

from step_impl.pages.login_page import LoginPage
from step_impl.pages.logout_page import LogoutPage
from step_impl.pages.reservation_page import ReservationPage


class PageFactory:
    driver = None
    login_page = None
    logout_page = None
    reservation_page = None

    
@before_suite
def init():
    PageFactory.driver = webdriver.Chrome()
    PageFactory.login_page = LoginPage(PageFactory.driver)   
    PageFactory.logout_page = LogoutPage(PageFactory.driver)
    PageFactory.reservation_page = ReservationPage(PageFactory.driver)


@after_suite
def close():
    PageFactory.driver.close()

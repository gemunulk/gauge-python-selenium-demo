from getgauge.python import before_suite, after_suite
from selenium import webdriver
import os  
from selenium.webdriver.chrome.options import Options  
import platform

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
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    #All the arguments added for chromium to work on selenium
    chrome_options.add_argument("--no-sandbox") #This make Chromium reachable
    chrome_options.add_argument("--no-default-browser-check") #Overrides default choices
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-default-apps") 

    if platform.system() == 'Darwin':
        chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' 
        path_to_chromedriver_binary = '/Users/gemunu/Documents/WebDriver/chromedriver'    
    elif platform.system() == 'Windows':
        pass
    else:   
        chrome_options.binary_location = '/usr/bin/chromium-browser' 
        path_to_chromedriver_binary = '/home/travis/virtualenv/python3.6.5/bin/chromedriver'
    
    #PageFactory.driver = webdriver.Chrome()
    PageFactory.driver = webdriver.Chrome(executable_path=path_to_chromedriver_binary,   chrome_options=chrome_options)
    PageFactory.login_page = LoginPage(PageFactory.driver)   
    PageFactory.logout_page = LogoutPage(PageFactory.driver)
    PageFactory.reservation_page = ReservationPage(PageFactory.driver)


@after_suite
def close():
    PageFactory.driver.close()
    PageFactory.driver.quit()

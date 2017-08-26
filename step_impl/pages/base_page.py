import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC



class BasePage(object):
    URL = os.getenv('APP_ENDPOINT')
    MAIN_URL = '{}/'.format(URL)

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))
        self.driver.find_element(*element).click()

    def set(self, element, value):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(value)

    def get(self, element):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))
        return self.driver.find_element(*element).text

    def get_attrubute_value(self, element):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))
        return self.driver.find_element(*element).get_attribute('value')

    def get_attrubute(self, element, attribute_name):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))
        return self.driver.find_element(*element).get_attribute(attribute_name)

    def get_selected_text_from_drop_down(self, locator):
        select = Select(WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable(locator)))
        return select.first_selected_option.text.strip()

    def hover(self, locator):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*locator))
        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()     

    def switch_to_top_window(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
        self.driver.maximize_window()
        time.sleep(5)

    def switch_to_frame(self, frame_reference):
        self.driver.switch_to_frame(frame_reference)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        #print(self.driver.page_source)


    def select(self, element, visible_text):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))
        select = Select(self.driver.find_element(*element))

        # FixMe
        try:
            select.select_by_visible_text(visible_text)
        except NoSuchElementException:
            time.sleep(5)
        finally:
            select.select_by_visible_text(visible_text)


    def get_tag_elements_in(self, element, tag_name):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))
        element = self.driver.find_element(*element)
        all_elements = element.find_elements_by_tag_name(tag_name)
        return all_elements

    def validate_page_title(self, expected_title):
        actual_title = str(self.driver.title)
        assert  actual_title == expected_title,"Incorrect page title "+actual_title

    def wait_until_element_no_loanger_visible(self, locator):
        WebDriverWait(self.driver, 100).until(EC.invisibility_of_element_located(locator))

    def is_selected(self, element):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))
        checked = self.driver.find_element(*element).is_selected()
        return checked

    def is_displayed(self, element):
        WebDriverWait(self.driver, 100).until(lambda driver: self.driver.find_element(*element))
        displayed = self.driver.find_element(*element).is_displayed()
        return displayed
    

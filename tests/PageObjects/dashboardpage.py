import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.Utils import common_util
from tests.Utils.common_util import webdriver_wait


class Dashboard:
    def __init__(self, driver):
        self.driver = driver



    #page locators

    page_heading = (By.XPATH, "//span[@data-qa = 'lufexuloga']")


    #page actions

    def get_dashboard_title(self):
        #webdriver_wait(driver=self.driver,element_tuple=self.get_dashboard_title())
        time.sleep(10)
        return self.driver.find_element(*Dashboard.page_heading)

    def get_dashboard_title_text(self):
        return self.get_dashboard_title().text






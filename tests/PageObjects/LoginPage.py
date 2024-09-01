import allure
import openpyxl
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.Utils.common_util import webdriver_wait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
import os

class LoginPage:
    def __init__(self,driver):
        self.driver = driver


    #page locators
    username = (By.ID, 'login-username')
    password =(By.ID, "login-password")
    login_btn = (By.ID,"js-login-btn")
    error_message = (By.ID, "js-notification-box-msg")




    #page_Actions
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_btn(self):
        return self.driver.find_element(*LoginPage.login_btn)

    def get_error_message(self):
        #webdriver_wait(driver=self.driver,element_tuple=self.get_error_message())
        print('I am in error message before wait')
        time.sleep(5)
        print('I am in error message after wait')
        return self.driver.find_element(*LoginPage.error_message)

    def get_error_message_text(self):
        print('I am in error message text')
        return self.get_error_message().text


    def vow_login(self,user,pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_login_btn().click()





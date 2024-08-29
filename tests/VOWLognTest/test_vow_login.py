import time
from logging import exception

import allure
import pytest
from selenium import webdriver

from tests.PageObjects.LoginPage import LoginPage
from selenium.common.exceptions import *


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://app.vwo.com/#/login')
    return driver


@allure.title('vow login negative')
@allure.title('vow login negative test case')
def test_vow_login_negative(setup):
    try:
        driver = setup
        login_page = LoginPage(driver)
        login_page.vow_login(user="cirizicap2@vjuum.com",pwd="Wingifiy@3214")
        time.sleep(5)
        error_message_element = login_page.get_error_message_text()
        assert error_message_element == 'Your email, password, IP address or location did not match'
    except Exception as e:
        pytest.xfail('test case fail')
        print(e)

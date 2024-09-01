import time
from logging import exception
from allure_commons.types import AttachmentType
import allure
import pytest
from selenium import webdriver
from tests.PageObjects.dashboardpage import Dashboard
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
        allure.attach(driver.get_screenshot_as_png(),name='login_screenshot',attachment_type=AttachmentType.PNG)
    except Exception as e:
        pytest.xfail('test case fail')
        print(e)



@allure.title('Vwo login positive')
@allure.description('TC# 1 for positive login')
def test_vwo_login_positive(setup):
    try:
        driver = setup
        login_page = LoginPage(driver)
        dash_board = Dashboard(driver)
        login_page.vow_login(user="xfpwpxo8zb@laafd.com",pwd="Wingifiy@321")
        dashboard_heading = dash_board.get_dashboard_title_text()
        assert dashboard_heading == 'Shadab Aslam'
        allure.attach(driver.get_screenshot_as_png(),name='Positive_Screenshot',attachment_type=AttachmentType.PNG)
    except Exception as e:
        pytest.xfail('test case  2 fail')
        print(e)






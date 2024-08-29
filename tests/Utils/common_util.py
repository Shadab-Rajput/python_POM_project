from asyncio import timeout

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def webdriver_wait(driver,element_tuple):
    WebDriverWait(driver=driver,timeout=10).until(
        EC.visibility_of_element_located(element_tuple)
    )

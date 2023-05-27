from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver

def driver_create():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    s = Service('C:/Users/.../.../chromedriver.exe')
    return webdriver.Chrome(service=s)


def wait_of_element_located(by, value, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (by, value)
        )
    )
    return element


def wait_of_element_located_xpath(xpath, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



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

class TestClass:
    
    def test_get_index_page(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")

        
        # Поиск и проверка попадания на главную страницу
        title_text = driver.find_element(by = By.CSS_SELECTOR, value="h1")
        assert title_text.text=="Добро пожаловать в сортировальню"

    def test_open_array(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")


        # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"3\"]', driver_init=driver)
        item_name.click()

        title_text = driver.find_element(by = By.CSS_SELECTOR, value="h1")
        assert title_text.text=="test1"
        
        driver.close()


    def test_target_search(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")

        # Поиск и ождиание прогрузки ссылки элемента test1 и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"3\"]', driver_init=driver)
        item_name.click()

        target_field = wait_of_element_located(by=By.CLASS_NAME, value="form-control", driver=driver)
        target_field.send_keys("3")
        
        submit_button = wait_of_element_located(by=By.ID, value="submit", driver=driver)
        submit_button.click()
        
        title_text = driver.find_element(by = By.CSS_SELECTOR, value="h2")
        assert title_text.text=="Позиция: 2"
        
        driver.close()

    

        

if __name__ == "__main__":
    pytest.main()

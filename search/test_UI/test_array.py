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


class TestClass:
    def setup_class(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        s = Service('C:/Users/.../.../chromedriver.exe')
        self.driver = webdriver.Chrome(options=options, service=s)
    
    
        
    def teardown_class(self):
        self.driver.close()

    def test_open_array(self):
        
        self.driver.get("http://127.0.0.1:5000")
        # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
        item_name = wait_of_element_located(by=By.ID, value='1', driver=self.driver)
        item_name.click()

        title_text = self.driver.find_element(by = By.CSS_SELECTOR, value="h1")
        assert title_text.text=="First array"




    def test_target_search(self):
        
        self.driver.get("http://127.0.0.1:5000")

        # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
        item_name = wait_of_element_located(by=By.ID, value='1', driver=self.driver)
        item_name.click()

        target_field = wait_of_element_located(by=By.CLASS_NAME, value="form-control", driver=self.driver)
        target_field.send_keys("3")
        
        submit_button = wait_of_element_located(by=By.ID, value="but", driver=self.driver)
        submit_button.click()
        
        title_text = self.driver.find_element(by = By.CSS_SELECTOR, value="h2")
        assert title_text.text=="Позиция: 2"

    def test_array_delete(self):
        
        self.driver.get("http://127.0.0.1:5000")

        # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
        item_name = wait_of_element_located(by=By.ID, value='1', driver=self.driver)
        item_name.click()

        target_field = wait_of_element_located(by=By.CLASS_NAME, value="form-control", driver=self.driver)
        target_field.send_keys("3")
        
        submit_button = wait_of_element_located(by=By.ID, value="but", driver=self.driver)
        submit_button.click()
        
        title_text = self.driver.find_element(by = By.CSS_SELECTOR, value="h2")
        assert title_text.text=="Позиция: 2"

        

if __name__ == "__main__":
    pytest.main()

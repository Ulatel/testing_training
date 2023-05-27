import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

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



if __name__ == "__main__":
    pytest.main()
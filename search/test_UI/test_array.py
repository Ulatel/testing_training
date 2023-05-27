import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import sqlite3

def insert_into_db(id, target, value):
    id = int(id)
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    array = conn.execute('SELECT * FROM arrays WHERE id = ?',
                        (id,)).fetchone()
    if array==None:
        conn.execute('INSERT INTO arrays (id, title, content) VALUES (?, ?, ?)',
                 (id, target, value))
    else:
        conn.execute('UPDATE arrays SET title = ?, content = ?'
                    ' WHERE id = ?',
                (target, value, id))
    conn.commit()
    conn.close()

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
    

    def test_open_array(self):
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")

    
        # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"300000\"]', driver_init=driver)
        item_name.click()

        title_text = driver.find_element(by = By.CSS_SELECTOR, value="h1")
        assert title_text.text=="UI TEST"
        
        driver.close()


    def test_target_search(self):
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")

        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")

        # Поиск и ождиание прогрузки ссылки элемента test1 и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"300000\"]', driver_init=driver)
        item_name.click()

        target_field = wait_of_element_located(by=By.CLASS_NAME, value="form-control", driver=driver)
        target_field.send_keys("3")
        
        submit_button = wait_of_element_located(by=By.ID, value="submit", driver=driver)
        submit_button.click()
        
        title_text = driver.find_element(by = By.CSS_SELECTOR, value="h2")
        assert title_text.text=="Позиция: 2"
        
        driver.close()

    
    def test_array_delete_alert(self):
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")

        # Поиск и ождиание прогрузки ссылки элемента test1 и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"300000\"]', driver_init=driver)
        item_name.click()

        delete_button = wait_of_element_located_xpath(xpath='//*[@id=\"delete\"]', driver_init=driver)
        delete_button.click()
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        alert = wait.until(EC.alert_is_present())

        # Store the alert text in a variable
        text = alert.text
        assert text == "Ты действительно хочешь удалить этот великолепный массив?"
        alert.dismiss()

        driver.close()

    def test_array_delete_alert_submit(self):
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")

        # Поиск и ождиание прогрузки ссылки элемента test1 и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"300000\"]', driver_init=driver)
        item_name.click()

        delete_button = wait_of_element_located_xpath(xpath='//*[@id=\"delete\"]', driver_init=driver)
        delete_button.click()
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        alert = wait.until(EC.alert_is_present())

        # Press the OK button
        alert.accept()
        
        #Мы точно на главной?
        title_text = driver.find_element(by = By.CSS_SELECTOR, value="h1")
        assert title_text.text=="Добро пожаловать в сортировальню"

        driver.close()
    
    def test_array_delete_alert_submit_check_deleted_array(self):
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")

        # Поиск и ождиание прогрузки ссылки элемента test1 и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"300000\"]', driver_init=driver)
        item_name.click()

        delete_button = wait_of_element_located_xpath(xpath='//*[@id=\"delete\"]', driver_init=driver)
        delete_button.click()
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        alert = wait.until(EC.alert_is_present())

        # Press the OK button
        alert.accept()

        item_name = wait_of_element_located_xpath(xpath='//*[@class=\"alert alert-danger\"]', driver_init=driver)
        assert item_name.text=='"UI TEST" was successfully deleted!'
        driver.close()

    def test_array_edit_mod(self):
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")

        # Поиск и ождиание прогрузки ссылки элемента test1 и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"300000\"]', driver_init=driver)
        item_name.click()

        edit_button = wait_of_element_located_xpath(xpath='//*[@id=\"edit\"]', driver_init=driver)
        edit_button.click()
        
        title_text = driver.find_element(by = By.CSS_SELECTOR, value="h1")
        assert title_text.text=='Edit "UI TEST"'

    def test_array_editing(self):
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        s = Service('C:/Users/.../.../chromedriver.exe')
        driver = webdriver.Chrome(service=s)
        driver.get("http://127.0.0.1:5000")

        # Поиск и ождиание прогрузки ссылки элемента test1 и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"300000\"]', driver_init=driver)
        item_name.click()

        edit_button = wait_of_element_located_xpath(xpath='//*[@id=\"edit\"]', driver_init=driver)
        edit_button.click()

        target_field = wait_of_element_located(by=By.CLASS_NAME, value="form-control", driver=driver)
        target_field.send_keys(" EDIT")
        
        submit_button = wait_of_element_located(by=By.ID, value="submit", driver=driver)
        submit_button.click()
        
        #time.sleep(5)
        title_text = driver.find_element(by = By.CSS_SELECTOR, value="h1")
        assert title_text.text=='UI TEST EDIT'

if __name__ == "__main__":
    pytest.main()

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_of_element_located(id, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, id)
        )
    )
    return element

def test_open_array():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/.../.../chromedriver.exe')
    driver.get("http://127.0.0.1:5000")

     # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
    item_name = wait_of_element_located(id='1', driver=driver)
    item_name.click()

    title_text = driver.find_element(by = By.CSS_SELECTOR, value="h2")
    assert title_text.text=="First array"

    driver.close()


if __name__ == '__main__':
    test_open_array()
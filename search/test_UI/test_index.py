import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def first_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/.../.../chromedriver.exe')
    driver.get("http://127.0.0.1:5000")

    
    # Поиск и проверка попадания на главную страницу
    title_text = driver.find_element(by = By.CSS_SELECTOR, value="h1")
    if title_text.text=="Добро пожаловать в сортировальню":
        print("Мы попали на главную страницу")
    else:
        print("Ошибка поиска элемента")

    time.sleep(5)


if __name__ == '__main__':
    first_test()
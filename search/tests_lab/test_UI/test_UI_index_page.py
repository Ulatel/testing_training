from utils import *
from tests_lab.test_UI.UI_utils import *


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
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")
        driver = driver_create()
        driver.get("http://127.0.0.1:5000")

    
        # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
        item_name = wait_of_element_located_xpath(xpath='//*[@id=\"300000\"]', driver_init=driver)
        item_name.click()

        title_text = driver.find_element(by = By.CSS_SELECTOR, value="h1")
        assert title_text.text=="UI TEST"
        
        driver.close()



"""if __name__ == "__main__":
    pytest.main()"""
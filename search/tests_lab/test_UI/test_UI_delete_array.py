from utils import *
from tests_lab.test_UI.UI_utils import *


class TestClass:
        
    def test_array_delete_alert(self):
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")
        
        driver = driver_create()
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
        
        driver = driver_create()
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
        
        driver = driver_create()
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


"""if __name__ == "__main__":
    pytest.main()
"""
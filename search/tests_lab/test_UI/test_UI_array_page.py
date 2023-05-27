from utils import *
from tests_lab.test_UI.UI_utils import *


class TestClass:
    
    def test_target_search(self):
        insert_into_db(id=300000, target="UI TEST", value="1 2 3")

        driver = driver_create()
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

    

"""if __name__ == "__main__":
    pytest.main()
"""
import pytest
import sqlite3
import api
#from api.app import get_db_connection
from api.lib.apiwrapper import *

# content of test_sample.py
class TestClass:
    def test_get_form_http_status_code(self):
        assert get_array_list().status_code == 200

    def test_post_form_http_status_code(self):
        assert post_create_array(title="test1", content="1 2 3").status_code == 200

    def test_post_null_form_http_status_code(self):
        assert post_create_array(title=None, content=None).status_code == 500

    def test_post_form_edit_http_status_code(self):
        assert post_edit_array(id = '6', title="test2", content="1 2 3").status_code == 200

    def test_post_nan_form_edit_http_status_code(self):
        assert post_edit_array(id = '5', title="test2", content="1 2 3").status_code == 200

    def test_post_form_delete_http_status_code(self):
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        conn.execute('INSERT INTO arrays (id, title, content) VALUES (?, ?, ?)',
                    (3, "title", "1 2 3"))
        conn.commit()
        conn.close()
        assert post_delete_array(id = '3').status_code == 200

    def test_post_form_delete_deleted_post_http_status_code(self):
        assert post_delete_array(id = '3').status_code == 500

    def test_post_form_delete_uncorrect_id_post_http_status_code(self):
        assert post_delete_array(id = '-3').status_code == 404

if __name__ == "__main__":
    pytest.main()
    
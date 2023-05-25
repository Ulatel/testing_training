import pytest
import sqlite3
import api
# from api.app import get_db_connection
from api.lib.apiwrapper import *

# content of test_sample.py


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


class TestClass:
    """
    def test_get_form_get_list_http_status_code(self):
        assert get_array_list().status_code == 200

    def test_post_form_create_http_status_code(self):
        assert post_create_array(title="test1", content="1 2 3").status_code == 200

    def test_post_null_form_http_status_code(self):
        assert post_create_array(title=None, content=None).status_code == 500

#???
    def test_post_form_edit_http_status_code(self):
        id = '299'
        insert_into_db(id = id, target = "test2", value="1 2 3")
        assert post_edit_array(id=id, title="test2_edit",
                               content="0 1 2 3").status_code == 200
        post_delete_array(id=id)
#???
    def test_post_form_delete_http_status_code(self):
        id = '300'
        insert_into_db(id = id,  target ="test3", value="1 2 3")
        assert post_delete_array(id=id).status_code == 200

    def test_post_form_delete_deleted_post_http_status_code(self):
        id = '301'
        assert post_delete_array(id=id).status_code == 500

    def test_post_form_delete_uncorrect_id_post_http_status_code(self):
        id = '-3'
        assert post_delete_array(id=id).status_code == 404

    def test_id_post_http_status_code(self):
        id = '302'
        insert_into_db(id, "test4", "4 5 6 7 0 1 2")
        parametrs = ['0', '3', '1']
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 200
    
    def test_id_post_nums_length_out_of_range_http_status_code(self):
        nums_int = list(range(10, 5000+1))+list(range(1, 10))
        nums = ''
        for i in nums_int:
            nums += str(i)+" "
        id = 303
        insert_into_db(id, "test5", nums)
        parametrs = ['100', '-100']
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 200

    def test_id_post_nums_double_error_http_status_code(self):
        nums = "1 1"
        id = 304
        insert_into_db(id, "test6", nums)
        parametrs = [
            10,
            -1,
            100,
        ]
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500


    def test_id_post_nums_length_out_of_range_min_error_http_status_code(self):
        nums = ""
        parametrs = [
            10,
            -1,
            100,
        ]
        id = 305
        insert_into_db(id, "test7", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500

    def test_id_post_nums_length_out_of_range_max_error_http_status_code(self):
        nums_int = list(range(10, 5001+1))+list(range(1, 10))
        nums = ""
        for num in nums_int:
            nums += str(num)+" "
        parametrs = [
            10,
            -100,
            100
            ]
        id = 306
        insert_into_db(id, "test8", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500

    def test_id_post_nums_value_in_range_min_http_status_code(self):
        nums = "-8888 100 10000 -9999"
        parametrs = [100, -8888, 9999, 1]
        id = 310
        insert_into_db(id, "test10", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 200
        
    def test_id_post_nums_value_in_range_max_http_status_code(self):
        nums = "-8888 100 -10000 -9999"
        parametrs = [100, -8888, 9999, 1]
        id = 311
        insert_into_db(id, "test11", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 200


    def test_id_post_nums_value_out_of_range_min_http_status_code(self):
        nums = "-8888 100 10001 -9999"
        parametrs = [100, -8888, 9999, 1]
        id = 312
        insert_into_db(id, "test12", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500
        
    def test_id_post_nums_value_out_of_range_max_http_status_code(self):
        nums = "-8888 100 -10001 -9999"
        parametrs = [100, -8888, 9999, 1]
        id = 313
        insert_into_db(id, "test13", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500

    def test_id_post_targer_in_range_http_status_code(self):
        nums = "-8888 100 10000 -10000"
        parametrs = [10000, -10000]
        id = 314
        insert_into_db(id, "test14", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 200
        

    def test_id_post_targer_of_rangehttp_status_code(self):
        nums = "-8888 100 10000 -9999"
        parametrs = [100000, -1000000, 9999999]
        id = 315
        insert_into_db(id, "test15", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500
    
    def test_id_post_non_unique_value_target_in_array_error(self):
        nums = [
            "1 1 2 3 4 5",
            "1 2 2 3 4 5",
            "4 5 6 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2",
            "1 1",
        ]
        target = 1
        id = 316
        for num in nums:
            insert_into_db(id, "test16", num)
            assert post_pos_target_in_array(id=id, target = target).status_code == 500
"""
    def test_post_create_form_non_sorted_values_in_nums_error(self):
        nums = [
            "1 2 3 1 2 3 1 2 3",
        ]
        id = 317
        for num in nums:
            insert_into_db(id, "test17", num)
            assert post_create_array(title="test17", content=num).status_code == 500
    
'''

################################
    # nums is an ascending array that is possibly rotated
    def test_id_post_non_sorted_values_in_nums_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([3, 7, 4, 5, 6, 1, 2], 10)

################################
    # nums is array is not integer

    def test_id_post_string_values_in_nums_error(self):
        sut = Solution()
        nums = [3, 's', 5, 6, 1, 2]
        parametrs = [10, 's', 'a', 5, 1]
        for target in parametrs:
            with self.assertRaises(TypeError):
                sut.search(nums, target)

    def test_id_post_float_values_in_nums_error(self):
        sut = Solution()
        nums = [3, 4.5, 5, 6, 1, 2]
        parametrs = [10, 4.5, 5.4, 1]
        for target in parametrs:
            with self.assertRaises(TypeError):
                sut.search(nums, target)

    def test_id_post_bool_values_in_nums_error(self):
        sut = Solution()
        nums = [3, True, 5, 6, 1, 2]
        parametrs = [10, True, 3]
        for target in parametrs:
            with self.assertRaises(TypeError):
                sut.search(nums, target)


if __name__ == "__main__":
    unittest.main()

    '''
if __name__ == "__main__":
    pytest.main()

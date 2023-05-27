from utils import insert_into_db
from api.lib.apiwrapper import *

# content of test_sample.py


class TestClass:

    def setup_module(self):
        print("Выполнение метода Setup_module")

    def teardown_module(self):
        print("Выполнение метода Teardown_module")


####GET LISTS FORM TEST
    def test_get_form_get_list_http_status_code(self):
        assert get_array_list().status_code == 200


####CREATE ARRAY FORM TESTS
    def test_post_create_form_http_status_code(self):
        assert post_create_array(title="test1", content="1 2 3").status_code == 200

    def test_post_null_form_http_status_code(self):
        assert post_create_array(title=None, content=None).status_code == 500
        assert post_create_array(title="Test2", content=None).status_code == 500
        assert post_create_array(title=None, content="1 2 3").status_code == 500
    
    def test_post_create_form_non_unique_value_target_in_array_error(self):
        nums = [
            "1 1 2 3 4 5",
            "1 2 2 3 4 5",
            "4 5 6 1 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2",
            "1 1",
        ]
        for num in nums:
            assert post_create_array(title="test2", content=num).status_code == 500

    def test_post_create_form_non_sorted_values_in_nums_error(self):
        nums = [
            "1 2 3 1 2 3 1 2 3",
            "3 4 5 0 999 123 1 2 0",
        ]
        for num in nums:
            assert post_create_array(title="test3", content=num).status_code == 500


    def test_post_create_form_nums_value_out_of_range_http_status_code(self):
        nums = [
            "10000000 0 1",
            "-10000000 0 1",
            " "
        ]
        nums_int = list(range(10, 50001+1))+list(range(1, 10))
        nums_long = ""
        for num in nums_int:
            nums_long += str(num)+" "
        nums.append(nums_long)

        for num in nums:
            assert post_create_array(title="test4", content=num).status_code == 500

    def test_post_create_form_nums_value_not_int_http_status_code(self):
        nums = [
            "10 0 s 1",
            "10 0 2.4 1",
            "-10 0 True 1",
            "a b c d",
        ]
        
        for num in nums:
            assert post_create_array(title="test5", content=num).status_code == 500

####DELETE ARRAY FORM TESTS
    def test_post_form_edit_http_status_code(self):
        id = '306'
        insert_into_db(id = id, target = "test6", value="1 2 3")
        assert post_edit_array(id=id, title="test6_edit",
                               content="0 1 2 3").status_code == 200
        post_delete_array(id=id)

    def test_post_form_delete_http_status_code(self):
        id = '307'
        insert_into_db(id = id,  target ="test7", value="1 2 3")
        assert post_delete_array(id=id).status_code == 200

    def test_post_form_delete_deleted_post_http_status_code(self):
        id = '308'
        assert post_delete_array(id=id).status_code == 500

    def test_post_form_delete_uncorrect_id_post_http_status_code(self):
        id = '-3'
        assert post_delete_array(id=id).status_code == 404


####ARRAY TARGET FORM TESTS

    def test_id_post_http_status_code(self):
        id = '309'
        insert_into_db(id, "test9", "4 5 6 7 0 1 2")
        parametrs = ['0', '3', '1']
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 200
    
    def test_id_post_nums_length_out_of_range_http_status_code(self):
        nums_int = list(range(10, 5000+10))+list(range(1, 10))
        nums = ''
        for i in nums_int:
            nums += str(i)+" "
        id = 310
        insert_into_db(id, "test10", nums)
        parametrs = ['100', '-100']
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500

    def test_id_post_nums_double_error_http_status_code(self):
        nums = "1 1"
        id = 311
        insert_into_db(id, "test11", nums)
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
        id = 312
        insert_into_db(id, "test12", nums)
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
        id = 313
        insert_into_db(id, "test13", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500

###range tests for target
    def test_id_post_nums_value_in_range_min_http_status_code(self):
        nums = "-8888 100 10000 -9999"
        parametrs = [100, -8888, 9999, 1]
        id = 314
        insert_into_db(id, "test14", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 200
        
    def test_id_post_nums_value_in_range_max_http_status_code(self):
        nums = "-8888 100 -10000 -9999"
        parametrs = [100, -8888, 9999, 1]
        id = 315
        insert_into_db(id, "test15", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 200


    def test_id_post_nums_value_out_of_range_min_http_status_code(self):
        nums = "-8888 100 10001 -9999"
        parametrs = [100, -8888, 9999, 1]
        id = 316
        insert_into_db(id, "test16", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500

    def test_id_post_nums_value_out_of_range_max_http_status_code(self):
        nums = "-8888 100 -10001 -9999"
        parametrs = [100, -8888, 9999, 1]
        id = 317
        insert_into_db(id, "test17", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500

    def test_id_post_targer_in_range_http_status_code(self):
        nums = "-8888 100 10000 -10000"
        parametrs = [10000, -10000]
        id = 318
        insert_into_db(id, "test18", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 200
        

    def test_id_post_targer_out_of_range_http_status_code(self):
        nums = "-8888 100 10000 -9999"
        parametrs = [100000, -1000000, 9999999]
        id = 319
        insert_into_db(id, "test19", nums)
        for target in parametrs:
            assert post_pos_target_in_array(id=id, target = target).status_code == 500



"""if __name__ == "__main__":
    pytest.main()"""

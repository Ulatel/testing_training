from unittest import TestCase
import unittest
from api.solution import Solution

class TestSolution(TestCase):
    
    def test_solution_target_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([4,5,6,7,0,1,2],0), 4)

    def test_solution_target_not_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([4,5,6,7,0,1,2],3), -1)

    def test_solution_target_not_in_array2(self):
        sut = Solution()
        self.assertEqual(sut.search([1], 0), -1)

################################
    #1 <= nums.length <= 5000
    def test_solutoin_min_nums_length_target_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([2], 2), 0)

    def test_solutoin_min_nums_length_target_not_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([2], 0), -1)

    def test_solutoin_max_nums_length_target_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search(list(range(10, 5000+1))+list(range(1, 10)), 100), 90)

    def test_solutoin_max_nums_length_target_not_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search(list(range(10, 5000+1))+list(range(1, 10)), -100), -1)
    
    #Errors
    def test_solutoin_nums_length_out_of_range_min_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([], 10)

    def test_solutoin_nums_length_out_of_range_max_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search(list(range(10, 5001+1))+list(range(1, 10)), 100)

################################################################
    #-10^4 <= nums[i] <= 10^4
    def test_solutoin_min_nums_value_target_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([-8888,100,-10000,-9999], 100), 1)

    def test_solutoin_min_nums_value_target_not_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([-8888,100,-10000,-9999], 20), -1)

    def test_solutoin_max_nums_value_target_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([20,9999, 10000,10,11], 10), 3)

    def test_solutoin_max_nums_value_target_not_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([20,9999, 10000,10,11], 30), -1)

    #Errors
    def test_solutoin_nums_value_out_of_range_min_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([-8888,100,-10001,-9999], 100)

    def test_solutoin_nums_value_out_of_range_max_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([20,9999, 10001,10,11], 10)


################################
    #-10^4 <= target <= 10^4
    def test_solutoin_min_target_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([-8888,100,-10000,-9999], -10000), 2)

    def test_solutoin_min_target_not_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([-888,100,-1000,-999], 10000), -1)

    def test_solutoin_max_target_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([20,9999, 10000,10,11], 10000), 2)

    def test_solutoin_max_target_not_in_array(self):
        sut = Solution()
        self.assertEqual(sut.search([20,999, 1000,10,11], -10000), -1)

    #Errors
    def test_solutoin_target_out_of_range_min_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([-888,100,-1000,-999], -10001)

    def test_solutoin_target_out_of_range_max_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([20,999, 1000,10,11], 10001)

################################
    #All values of nums are unique
    def test_solutoin_non_unique_value_target_in_array_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([3,4,4,5,6,1,2], 10)

################################
    #nums is an ascending array that is possibly rotated
    def test_solutoin_non_sorted_values_in_nums_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([3,7,4,5,6,1,2], 10)

################################
    #nums is array is not integer
    def test_solutoin_string_values_in_nums_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([3,'s',5,6,1,2], 10)

    def test_solutoin_float_values_in_nums_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([3,4.5,5,6,1,2], 10)

    def test_solutoin_bool_values_in_nums_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([3, True ,5,6,1,2], 10)


if __name__ == "__main__":
  unittest.main()



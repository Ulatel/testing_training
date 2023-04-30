from unittest import TestCase
import unittest
from api.solution import Solution


class TestSolution(TestCase):

    def test_solution_target(self):
        sut = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        parametrs = [
            [0, 4],  # target in array
            [3, -1],  # target not in array
            [1, 5 ]  # target not in array
        ]
        for target, answer in parametrs:
            self.assertEqual(sut.search(nums, target), answer)

################################
    # 1 <= nums.length <= 5000
    def test_solutoin_nums_length_in_range(self):
        sut = Solution()
        nums = [2]
        parametrs = [
            [2, 0],  # target in array
            [0, -1]  # target not in array
        ]
        for target, answer in parametrs:
            self.assertEqual(sut.search(nums, target), answer)

    def test_solutoin_nums_length_in_range(self):
        sut = Solution()
        nums = list(range(10, 5000+1))+list(range(1, 10))
        parametrs = [
            [100, 90],
            [-100, -1]
        ]
        for target, answer in parametrs:
            self.assertEqual(sut.search(nums, target), answer)
    # Errors

    def test_solutoin_nums_length_out_of_range_min_error(self):
        sut = Solution()
        nums = []
        parametrs = [
            10,
            -1,
            100,
        ]
        for target in parametrs:
            with self.assertRaises(ValueError):
                sut.search(nums, target)

    def test_solutoin_nums_length_out_of_range_max_error(self):
        sut = Solution()
        nums = list(range(10, 5001+1))+list(range(1, 10))
        parametrs = [
            10,
            -100,
            100,
        ]

        for target in parametrs:
            with self.assertRaises(ValueError):
                sut.search(nums, target)


################################################################
    # -10^4 <= nums[i] <= 10^4


    def test_solutoin_nums_value_in_range_min(self):
        sut = Solution()
        nums = [-8888, 100, -10000, -9999]  # minimum
        parametrs = [
            [100, 1],  # target in array
            [-8888, 0],
            [-9999, 3],
            [20, -1]  # target not in array
        ]
        for target, answer in parametrs:
            self.assertEqual(sut.search(nums, target), answer)

    def test_solutoin_nums_value_in_range_max(self):
        sut = Solution()
        nums = [20, 9999, 10000, 10, 11]  # maximum
        parametrs = [
            [10, 3],
            [20, 0],
            [30, -1]
        ]
        for target, answer in parametrs:
            self.assertEqual(sut.search(nums, target), answer)

    # Errors

    def test_solutoin_nums_value_out_of_range_min_error(self):
        sut = Solution()
        nums = [-8888, 100, -10001, -9999]
        parametrs = [
            100,
            10,
            -10001
        ]
        for target in parametrs:
            with self.assertRaises(ValueError):
                sut.search(nums, target)

    def test_solutoin_nums_value_out_of_range_max_error(self):
        sut = Solution()
        nums = [20, 9999, 10001, 10, 11]
        parametrs = [
            100,
            10001,
            11,
            12,
            10
        ]
        for target in parametrs:
            with self.assertRaises(ValueError):
                sut.search(nums, target)


################################
    # -10^4 <= target <= 10^4


    def test_solutoin_target_in_range_min(self):
        sut = Solution()
        nums = [-8888, 100, -10000, -9999]
        parametrs = [
            [-10000, 2],  # target in array
            [10000, -1]  # target not in array
        ]
        for target, answer in parametrs:
            self.assertEqual(sut.search(nums, target), answer)

    def test_solutoin_target_in_range_max(self):
        sut = Solution()
        nums = [20, 9999, 10000, 10, 11]
        parametrs = [
            [10000, 2],
            [20, 0],
            [-10000, -1]
        ]
        for target, answer in parametrs:
            self.assertEqual(sut.search(nums, target), answer)

    # Errors

    def test_solutoin_target_out_of_range_error(self):
        sut = Solution()
        parametrs = [
            [[-888, 100, -1000, -999], -10001],
            [[20, 999, 1000, 10, 11], 10001]
        ]
        for nums, target in parametrs:
            with self.assertRaises(ValueError):
                sut.search(nums, target)


################################
    # All values of nums are unique


    def test_solutoin_non_unique_value_target_in_array_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([3, 4, 4, 5, 6, 1, 2], 10)

################################
    # nums is an ascending array that is possibly rotated
    def test_solutoin_non_sorted_values_in_nums_error(self):
        sut = Solution()
        with self.assertRaises(ValueError):
            sut.search([3, 7, 4, 5, 6, 1, 2], 10)

################################
    # nums is array is not integer
    def test_solutoin_string_values_in_nums_error(self):
        sut = Solution()
        parametrs = [
            [[3, 's', 5, 6, 1, 2], 10],
            [[3, 4.5, 5, 6, 1, 2], 10],
            [[3, True, 5, 6, 1, 2], 10]
        ]
        for nums, target in parametrs:
            with self.assertRaises(ValueError):
                sut.search(nums, target)

    def test_solutoin_string_values_in_nums_error(self):
        sut = Solution()
        nums = [3, 's', 5, 6, 1, 2]
        parametrs = [10, 's', 'a', 5, 1]
        for target in parametrs:
            with self.assertRaises(ValueError):
                sut.search(nums, target)

    def test_solutoin_float_values_in_nums_error(self):
        sut = Solution()
        nums = [3, 4.5, 5, 6, 1, 2]
        parametrs = [10, 4.5, 5.4, 1]
        for target in parametrs:
            with self.assertRaises(ValueError):
                sut.search(nums, target)

    def test_solutoin_bool_values_in_nums_error(self):
        sut = Solution()
        nums = [3, True, 5, 6, 1, 2]
        parametrs = [10, True, 3]
        for target in parametrs:
            with self.assertRaises(ValueError):
                sut.search(nums, target)


if __name__ == "__main__":
    unittest.main()

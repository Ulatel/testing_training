
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for num in nums:
            if type(num) != int:
                raise TypeError

        print(nums.index(min(nums)), range(nums.index(min(nums)) - 1))
        print(all(nums[i] <= nums[i+1]
              for i in range(nums.index(min(nums)) - 1)))
        if all(nums[i] <= nums[i+1] for i in range(nums.index(min(nums)) - 1)) != True or  all(nums[j] <= nums[j+1] for j in range(nums.index(min(nums)), len(nums)-1)) != True:
            raise ValueError

        if len(nums) < 1 or len(nums) > 5000:
            raise ValueError

        if max(nums) > 10000 or min(nums) < -10000:
            raise ValueError

        if target > 10000 or target < -10000:
            raise ValueError

        if len(nums) != len(set(nums)):
            raise ValueError
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

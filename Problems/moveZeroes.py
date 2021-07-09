# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        l = 0
        r = 1

        while r < len(nums):
            if nums[l] == 0:
                if abs(nums[r]) > abs(nums[l]):
                    nums[l], nums[r] = nums[r], nums[l]
                    l += 1
                r += 1
            else:
                l += 1
                r += 1
        
        return nums


# [1,0]
  # [0,1,0,3,12] --> [1,3,12,0,0]
  # [1,1,1,0,2,6,6] -->             


if __name__ == '__main__':
    digits = [0,1,0,3,12]
    digits2 = [1,0,1]
    solution = Solution()
    print(solution.moveZeroes(digits2))
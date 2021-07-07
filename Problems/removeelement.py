# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first 
# part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should 
# hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        k = 0
        r = len(nums)-1
        while l <= r:
            # print(nums)
            # print(nums[l], nums[r])
            if nums[l] == val:
                k += 1
                nums[l] = nums[r]
                nums[r] = '_'
                r -= 1
                if nums[l] != val:
                    l += 1              
            else:
                l += 1

        return len(nums)-k




# [3,2,2,3] l = 0 r = 3
# [_,2,2,3] l = 0 r = 3 if nums[r] = val, nums[r] = '_', r-= 1 nums[l]


# [0,1,2,2,3,0,4,2]
# ...
# [0,1,_,2,3,0,4,2]


if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    num = [1]
    val=2
    solution=Solution()
    print(solution.removeElement(nums, val))
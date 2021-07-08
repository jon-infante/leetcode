# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List

#Slow solution
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         found = set()
#         pt = 0
#         nums_remain = 0
#         while pt < len(nums):
#             if nums[pt] not in found:
#                 found.add(nums[pt])
#                 pt += 1
                
#             else:
#                 nums.pop(pt)
        
#         return pt
                
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        pt = 0

        for i in range(1,len(nums)):
            if nums[i] != nums[pt]:
                pt += 1
                nums[pt] = nums[i]
        
        return pt + 1




# [.0,.0,1,1,1,2,2,3,3,4] pt = 0
# [.0,0,.1,1,1,2,2,3,3,4] pt += 1 --> nums[pt(+1)] = nums[i]
# [0,.1,0,.1,1,2,2,3,3,4] pt
# [0,.1,0,1,.1,2,2,3,3,4] pt
# [0,.1,0,1,1,.2,2,3,3,4] pt += 1 --> nums[pt(+1)] = nums[i]
# [0,1,2,3,.4,0,2,.1,.3,.1] pt += 1
# [0,1,2,.1,1,0,.2,3,3,4] pt += 1



if __name__ == '__main__':
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums))
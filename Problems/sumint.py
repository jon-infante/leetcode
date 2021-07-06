from typing import List

# class Solution:
#     """ Time: O(n^2) Space: O(1)
#     """
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         if len(nums) < 2:
#             return None

#         left_p = 0
#         right_p = 1

#         searching = True
#         while searching:
#             for _ in range(len(nums) - 1):
#                 if nums[left_p] + nums[right_p] == target:
#                     return [left_p, right_p]
#                 else:
#                     right_p += 1
#                 #If both pointers are the same, we omit that combination [Must be different elements]
#                 if left_p == right_p:
#                     right_p += 1
#             #Reset right pointer and move the left points forward one
#             right_p = 0
#             left_p += 1

#             #If all combinations have been exhausted
#             if left_p == len(nums):
#                 searching = False

#         return None       
        
# 0,1 0,2 0,3 (omit 0,0)
# 1,0 1,2 1,3 (omit 1,1)
# 2,0 2,1 2,3 (omit 2,2)
# 3,0 3,1 3,2 (omit 3,3)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dicti:
                return [dicti[diff], i]
            else:
                dicti[num] = i




if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums,target))
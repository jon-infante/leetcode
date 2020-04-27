# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

class Solution:
    def search(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        #Initial boundaries
        min = 0
        max = len(nums) - 1
        #While the left pointer hasnt passed the right pointer
        while min < max:
            mid = (max + min) // 2
            #Checking if the target has been found
            if nums[mid] == target:
                return mid

            if nums[min] <= nums[mid]:
                if target >= nums[min] and target < nums[mid]:
                    max = mid - 1
                else:
                    min = mid + 1
            else:
                if target > nums[mid] and target <= nums[max]:
                    min = mid + 1
                else:
                    max = mid - 1
        #Checks if it was found again, this time for the min value
        if nums[min] == target:
            return min
        else:
            return -1

if __name__ == '__main__':
    lis = [8, 9, 11, 14, 0, 1, 2, 5, 7]
    searched = Solution()      
    print(searched.search(lis, 1))
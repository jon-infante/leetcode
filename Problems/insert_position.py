# Given a sorted array and a target value, return the index 
# if the target is found. If not, return the index where it 
# would be if it were inserted in order.

# You may assume no duplicates in the array.

class Solution:
    def searchInsert(self, nums, target):
        #Checking if it would be the first index in the list
        if target < nums[0]:
            return 0
        for i in range(len(nums)-1):
            if target > nums[i] and target <= nums[i+1]:
                return i+1
        #For if the number would be put at the end of the list
        return len(nums)


if __name__ == '__main__':
    lis1 = [1,3,5,6]
    search = Solution()
    print(search.searchInsert(lis1, 5))

        
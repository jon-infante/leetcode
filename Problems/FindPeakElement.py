# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

class Solution:
    def findPeakElement(self, nums):
        #Lowest number possible, to deal with negative numbers
        max = float("-inf")
        index = 0
        #Iterate over each number while saving its index
        for i, num in enumerate(nums):
            if num > max:
                max = num
                index = i
        
        return index



if __name__ == '__main__':
    solution = Solution()
    print(solution.findPeakElement([-2147483648,-2147483647]))
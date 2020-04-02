class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1
        #If the right pointer passes the left one
        while left < right:
            #Getting the minimum value of the two pointers, and multiplying to get the area
            container = min(height[left], height[right]) * (right - left)
            #Checking if there is a new highest area
            if container > maxarea:
                maxarea = container
            #Moving the pointers based off the value of them
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1

        return maxarea

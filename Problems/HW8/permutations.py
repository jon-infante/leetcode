class Solution:
    def permute(self, nums):
        """ Time complexity O(n^2)"""
        permutations = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)): 
            # get all permutations of subarray without current item
            perms = self.permute(nums[:i] + nums[i+1:])  
            for p in perms:
                permutations.append([nums[i], *p])
        return permutations

if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1,2,3]))
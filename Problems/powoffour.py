"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

#No math import
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """Since all power of fours are two power of twos, we first check if the number
        is greater than 0, then if n is power of 2, follower by if 1 less than n is divisible by 3. """
        return (n > 0) and (n & (n - 1) == 0) and ((n - 1) % 3 == 0)


# #First example solution
# import math

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         print(n**4)
#         print(math.log(n,4))
#         return n > 0 and math.log(n,4) % 1 == 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfFour())
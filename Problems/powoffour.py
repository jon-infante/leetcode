"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""


import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n,4) % 1 == 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfFour(1))
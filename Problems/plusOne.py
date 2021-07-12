# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

from typing import List

class Solution:
    def plusOne(self, digits: List[int], pos=None) -> List[int]:
        if not pos:
            pos = -1

        if digits[pos] != 9:
            digits[pos] += 1
            return digits
        else:   
            digits[pos] = 0
            if len(digits) + pos == 0:
                return ([1] + digits)
    
            return self.plusOne(digits,pos-1)



if __name__ == '__main__':
    yo = [0]
    d = [9,9]
    ok = [9,8,9]
    sols = [9]
    bal = [1,2,3]
    dog = [4,3,2,1]
    solution = Solution()
    print(solution.plusOne(sols))
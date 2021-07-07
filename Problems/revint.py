# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        elif x > 0:
            sign = 1
        else:
            return 0
        
        rev = sign * int((str(abs(x)))[::-1])
        if rev < -2**31 or rev > 2**31 -1:
            return 0
        
        return rev




if __name__ == '__main__':
    solution = Solution()
    inm = 120
    print(solution.reverse(inm))
# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
        
#         if str(x) == str(x)[::-1]:
#             return True
        
#         return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        x_len = self.getLength(x)

        if x_len == 1:
            return True

        iters = x_len // 2
        for i in range(iters):
            p = 10**(x_len-1-i)
            left = (x // p) % 10
            right = x % 10

            if left == right:
                x //= 10
                x_len -= 1
            else:
                return False

        return True

    def getLength(self, x: int) -> int:
        length = 0
        while x != 0:
            x = x // 10
            length += 1
        
        return length


if __name__ == '__main__':
    c = 2004
    b = 1000021
    yo = 1221
    p = 12321
    dog = 123212
    big = 12
    si = 11111111
    solution = Solution()
    print(solution.isPalindrome(p))

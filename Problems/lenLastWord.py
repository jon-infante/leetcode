# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = 0
        count = 0
        for char in s:
            if char == ' ' and count != 0:
                last = count
                count = 0
            else:
                if char != ' ':
                    count += 1
                    last = count
            
        return last


if __name__ == '__main__':
    c = "My bagel is nice and warm and creamy        "
    s = "Hello World"
    d = "adddd"
    t = " "
    p = "b   a    "
    solution = Solution()
    print(solution.lengthOfLastWord(s))
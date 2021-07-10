# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

#  Input: haystack = "hello", needle = "ll"
#  Output: 2



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        l = 0
        r = len(needle) - 1

        sliced = haystack[l:r+1]

        while r < len(haystack):
            if sliced == needle:
                return l
            l += 1
            r += 1

            slice = haystack[l:r+1]


# 'ab'  'a'
# 


if __name__ == '__main__':
    h1 = "mississippi"
    n1 = "issip"
    hs = 'aaaaa'
    nd = 'bba'
    hs2 = "hello"
    nd2 = "ll"
    hs3 = 'aaa'
    nd3 = 'aaaa'
    solution = Solution()
    print(solution.strStr(hs2,nd2))
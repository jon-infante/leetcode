class Solution:
    def isAnagram(self, s, t):
        if self.findLetters(s) == self.findLetters(t):
            print(self.findLetters(s))
            print(self.findLetters(t))
            return True
        return False

    def findLetters(self, word):
        contains = {}
        for l in word:
            if l not in contains:
                contains[l] = 1
            else:
                contains[l] += 1


        




if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram('a', 'b'))
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number 
# could represent. Return the answer in any order.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# 1 = None, 2 = 'abc', 3 = 'def', 4 = 'ghi', 5 = 'jkl', 6 = 'mno', 7 = 'pqrs', 8 = 'tuv', 9 = 'wxyz'

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        mapper = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


        # for i in range(1, len(digits)):
        #     outputs = [char + ending for char in outputs for ending in mapper[digits[i]]]
        

        output = ['']

        for dig in digits:
            new_output = []
            for i in output:
                for j in mapper[dig]:
                    new_output.append(i+j)
                    # print(new_output)
            output = new_output

        return output


# digits = "29"
# 'abc' and 'wxyz'



# [0,0] and [1,0], 
# [0,0] and [1,1], 
# [0,0] and [1,2]
# [0,0] and [1,3]
# [1,0] and [1,0], 
# [1,0] and [1,1], 
# [1,0] and [1,2]
# [2,0] and [1,0], 
# [2,0] and [1,1], [2,0] and [1,2]


# [0,0][0,1][0,2]
# [1,0][1,1][1,2]
# [2,0][2,1][2,2]
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]


if __name__ == '__main__':
    digits = "239"
    solution = Solution()
    print(solution.letterCombinations(digits))
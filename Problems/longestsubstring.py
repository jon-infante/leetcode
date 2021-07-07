# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        if len(s) == 1: return 1

        max = 1
        cur_max = 1
        l_p = 0
        r_p = 1
        char_index = {s[l_p]: l_p}
        while r_p < len(s):
            print(l_p, r_p)
            print(char_index)
            if s[r_p] not in char_index:
                char_index[s[r_p]] = r_p #Saving current index of most recent unique letter
                r_p += 1
            else:
                l_p = char_index[s[r_p]] + 1 #Change left pointer to where we found the last matching element
                char_index[s[r_p]] = r_p
                r_p += 1
            
            cur_max = (r_p) - l_p
            
            if cur_max > max:
                max = cur_max

            
        return max
'abcabcbb'

# c_i[a] = 0,
#l_p = 0, r_p = 1 --> c_i[b] = 1: max = 1+1
#l_p = 0, r_p = 2 --> c_i[c] = 2: max = 2+1
#l_p = 0, r_p = 3 --> l_p = c_i[a] + 1 : c_i[a] = l_p:1
#l_p = 1, r_p = 4 --> l_p = c_i[b] + 1 : c_i[b] = l_p:2
#l_p = 2, r_p = 5 --> l_p = c_i[c] + 1 : c_i[c] = l_p:3
#l_p = 3, r_p = 6 --> l_p = c_i[b](4) + 1 = 5 : l_p = c_i[b]:5
#l_p = 5, r_p = 7




# if letter is not in the set
# add it to a set
# Replace dictionary input[letter] equal to its index position
# One we reach a certain letter and we've seen that letter before, 
#   we then move our left pointer 1 ahead of the previous matched letter we found
# replace dictionary input[letter] equal to its index position
#then continue to move right pointer
# use length of left pointer and right pointer for max output




if __name__ == '__main__':
    solution = Solution()
    s = "abcabcbb"
    t = "bbbbb"
    g = "pwwkew"
    print(solution.lengthOfLongestSubstring(g))
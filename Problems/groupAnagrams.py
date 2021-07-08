# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically 
# using all the original letters exactly once.

from typing import List

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         if strs is None or len(strs) == 0:
#             return []
#         ana_dict = {}
#         ana_list = []
#         for word in strs:
#             word_dict = {}
#             for let in word:
#                 if let in word_dict:   
#                     word_dict[let] += 1
#                 else:
#                     word_dict[let] = 1
#             #Initially populate the dictionary with the first anagram
#             if ana_dict == {}:
#                 #0 initially for the first index in the ana_list
#                 ana_dict['0'] = word_dict
#                 ana_list += [word]
            
#             for w in ana_dict:
#                 print(ana_dict)
#                 if ana_dict[w] == word_dict:
#                     ana_list[int(w)] += word
#                 else:
#                     ana_dict[len(ana_list)] = word_dict
#                     ana_list += [word]
#                     break

        
#         return ana_list

                

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  
        if strs is None or len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        anagrams = []
        found = {}
        pos = 0
        for st in strs:
            org_st = st
            st = ''.join(sorted(st))
            if st in found:
                anagrams[found[st]].append(org_st)
            else:
                found[st] = pos
                anagrams.append([org_st])
                pos += 1

        return anagrams


    # strs2 = ["eat","tea","tan","ate","nat","bat"]


# ["eat", "tea", "tan"]
# [eat] = {e: 1, a: 1, t: 1} 
# []




if __name__ == '__main__':
    strs3 = [""]
    strs2 = ["eat","tea","tan","ate","nat","bat"]
    strs = ["eat", "tea", "tan"]
    solution = Solution()
    print(solution.groupAnagrams(strs2))
    pass      


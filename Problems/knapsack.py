# from typing import List

# #dp

# class Solution:
#     def lastStoneWeightII(self, stones: List[int]) -> int:
#         total = sum(stones)
        
#         Max_weight = int(total/2)
        
#         current = (Max_weight+1)*[0]
#         for v in stones:
#             for w in range(Max_weight, -1, -1):
#                 if w-v>=0:
#                     current[w] = max(v + current[w-v], current[w])
#                     print(current)
           
#         return total-2*current[-1]



# if __name__ == '__main__':
#     stones = [2,7,4,1,8,1]
#     solution = Solution()
#     print(solution.lastStoneWeightII(stones))
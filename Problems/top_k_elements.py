class Solution:
    def topKFrequent(self, nums, k):
        count = dict()
        top_k_list = []
        
        for num in nums:
            count[num] = 1 if num not in count else count[num] +1
            
        while len(top_k_list) < k:
            top_num = max(count, key = lambda x: count[x])
            top_k_list.append(top_num)
            del count[top_num]
                              
        return top_k_list
        
if __name__ == '__main__':
    solution = Solution()
    print(solution.topKFrequent([1,1,1,2,2,3], 2))
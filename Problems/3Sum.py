from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unfound = True
        solution_list = []
        set_list = []
        curr_i = 0
        curr_j = 1
        curr_k = 2

        if not nums:
            return []
        if nums == [0] or nums == [] or len(nums) < 3:
            return []


        while unfound:
            #If a triplets solution is found, save to list of solutions
            sequence = [nums[curr_i],nums[curr_j],nums[curr_k]]
            if sequence not in solution_list and set(sequence) not in set_list:
                if sequence[0] + sequence[1] + sequence[2] == 0:
                    #Sort sequence
                    if sequence[0] > sequence[1]:
                        sequence[0], sequence[1] = sequence[1], sequence[0]
                    if sequence[1] > sequence[2]:
                        sequence[1], sequence[2] = sequence[2], sequence[1]
                        if sequence[0] > sequence[1]:
                            sequence[0], sequence[1] = sequence[1], sequence[0]
                    #Adds to list of solutions
                    solution_list.insert(0,sequence)
                    set_list.append(set(sequence))
            #If the last sequence has been reached
            if curr_i == (len(nums) - 3) and curr_j == (len(nums) - 2) and curr_k == (len(nums) - 1):
                solution_list.sort()
                return solution_list
            #Once k has reached its peak position, increment j and position k after j. repeating for i and j. Increment k otherwise
            if curr_k == len(nums) - 1:
                curr_j += 1
                curr_k = curr_j + 1
            else:
                curr_k += 1
            if curr_j == len(nums) - 2:
                curr_i += 1
                curr_j = curr_i + 1
                curr_k = curr_j + 1

            
        

if __name__ == '__main__':
    ok = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
    zeros = [0,0,0,0]
    nums0 = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    nums = [-1,0,1,2,-1,-4]
    nums2 = [-1,0,1]
    nums3 = [0]
    solution = Solution()
    print(solution.threeSum(ok))
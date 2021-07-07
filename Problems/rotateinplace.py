from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        store = {}
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                store[(j,len(matrix)-1-i)] = matrix[i][j]

        for ind, val in store.items():
            matrix[ind[0]][ind[1]] = val

        return matrix

if __name__ == '__main__':
    mat3 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    mat1 = [[1]]
    mat2 = [[1,2],[3,4]]
    solution=Solution()
    print(solution.rotate(mat3))





# [0,0] --> [0,2] val 1
# [0,1] --> [1,2] val 2
# [0,2] --> [2,2] val 3
# [1,0] --> [0,1] val 4
# [1,1] --> [1,1] val 5
# [1,2] --> [2,1] val 6
# [2,0] --> [0,0] val 7
# [2,1] --> [1,0] val 8
# [2,2] --> [2,0] val 9


#         """
# for i in range(len(matrix)-1)
#     for j in range(len(matrix)-1)
#  [1,2,3] [4,5,6] [7,8,9]       
# >[7,2,3] [4,5,6] [1,8,9] --> [0i,0j] swapped with [len(matrix)-1-0j,0]
# >[7,4,3] [2,5,6] [1,8,9] --> [0i,1j] swapped with [len(matrix)-1-1j,0]
# >[7,4,1] [2,5,6] [3,8,9] --> [0i,2j] swapped with [len(matrix)-1,0]  
# --
# >[7,4,1] [8,5,6] [3,2,9] --> [1i,0j] swapped with [len(matrix)-1,1]
# >[7,4,1] [8,]
        
        
#         """

#The first matrix's numbers correspond with the last digits of each output list.
# repeat for the next input list to apply to the 2nd to last digits in each output list

# input = [123] [456] [789]
# output = [741] [852] [963] 
### INCOMPLETE

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix, target):
        """Given a sorted matrix, ascending from left to right, find the target value.
        
        matrix: list
        """
        #If the matrix doesn't exist
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        #If the first element of the matrix is the target
        if matrix[0][0] == target:
            return True
        left = 0
        #Last number in the matrix
        right = (len(matrix[0])*len(matrix))-1
        #Until the binary search is complete
        while left <= right:
            #Between the two pointers
            index = (left + right) // 2
            #Converting the index to the corresponding matrix indices
            mat_x, mat_y = self.matrixConvert(matrix, index)
            if matrix[mat_x][mat_y] < target:
                #Set the left pointer to where the target was and shift to the right
                left = index + 1
            elif matrix[mat_x][mat_y] > target:
                #Set the right pointer to where the target was and shift to the left
                right = index - 1
            else:
                #Target found
                return True
        #Target not found
        return False

    def matrixConvert(self, matrix, index):
        """Convert from integer index to matrix indices

        matrix: list
        index: int
        """
        x, y = divmod(index, len(matrix)+1)
        #Edge cases where the length of the lists are 1 
        if len(matrix[0]) == 1:
            if len(matrix) == 1:
                return 0,0
            return x+1,0

        return x,y


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchMatrix([[1], [3]], 1))
    # print(solution.matrixConvert([[1, 3, 5 ,7], [10, 11, 16, 20], [23, 30, 34, 50]], 8))
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix):
        """Given a matrix, return the elemnts of the matrix in a clockwise order.
        
        matrix: list
        """
        spiral = []
        positive = True
        x = 0
        y = -1
        #Used to set boundaries of the spiral
        if matrix:
            lim_x = len(matrix) - 1
            lim_y = len(matrix[0])
        else:
            return []

        #While all the elements of the matrix are not in the new list
        while len(spiral) != (len(matrix) * len(matrix[0])):
             #Traversing y steps based off of the current spiral limit
            for j in range(lim_y):
                if positive:
                    y += 1
                else:
                    y -= 1
                spiral.append(matrix[x][y])
            #Decreasing the next leg of the spiral
            lim_y -= 1
            #Traversing x steps based off of the current spiral limit
            for i in range(lim_x):
                if positive:
                    x += 1
                else:
                    x -= 1
                print(matrix[x][y])
                spiral.append(matrix[x][y])
               
            #Decreasing the next leg of the spiral
            lim_x -= 1
            
            #Switching rotation of spiral for x and y
            if positive:
                positive = False
            else:
                positive = True
        
        return spiral


if __name__ == '__main__':
    solution = Solution()
    print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, intx):
        """Returns the square root of a given number. Increments the root up and down
        until it gets a precise measurement.
        
        int: intx
        float: root, increment
        """
        #Returns 1 if the input is 1, square root of itself
        if intx == 1:
            return 1
        
        beginning = True
        root = 0
        #Scale to add or subtract decimal numbers from the root number
        increment = 1

        #If the square root hasn't been found yet and it hasn't gone to a precise enough root yet
        while root**2 != intx:
            print(root)
            #When the increment gets below 1/10, we go to return the integer of this number
            if increment < 1/10:
                break
            #If we passed the square root number
            if root**2 > intx:
                #Changing beginning so we do not increase the increment ever again.
                beginning = False
                #Decrease the root by the determined decimal increment
                root -= increment
                #Changing the increment scale by a factor of 10
                increment = increment/10
            else:
                if beginning:
                    #Changing the increment scale by a factor of 10
                    increment = increment*10
                #Increase the root by the determined decimal increment
                root += increment
                #Determining the scale of the number to get a more fitting increment
                
                

        return int(root)
      

if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(1999))
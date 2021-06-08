"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #0 and 1 are perfect squares
        if num == 0 or num == 1:
            return True
        #Counter
        i = 1
        #Current iteration squared to see if num has been passed
        while (i**2) < num:
            i += 1
            #Checking for a perfect square
            if i**2 == num:
                return True
        #No perfect square has been found
        return False


"""
Pythonic Solution

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return ((num**0.5) % 1 == 0) 
"""

"""
C++ log(n) solution

class Solution {
public:
    bool isPerfectSquare(int num) {
        int start=1;
        int end=num;
        while(start<=end){
            double mid=start+(end-start)/2;
            double val=num/mid;
            if(mid==val) return true;
            if(mid<val) start=mid+1;
            else end=mid-1;
        }
        return false;
    }
};
"""
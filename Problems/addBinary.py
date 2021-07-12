# Given two binary strings a and b, return their sum as a binary string.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Set the longer string to a
        if len(b) > len(a):
            a, b = b, a

        carry = 0
        output = ''
        for i in range(len(a)):
            #Check if the b string is still iterable
            if i < len(b):
                b_num = int(b[len(b)-1-i])
            else:
                b_num = 0
    
            roll_over = (int(a[len(a)-1-i]) + b_num + carry)
            output += str(roll_over % 2)
            carry = 0

            if roll_over >= 2:
                carry += 1
            
        if carry == 1:
            return '1' + output[::-1]
        
        return output[::-1]


# a = '11' + b = '1' = '100'
# a = '11' + b = '11' = '110'
        
if __name__ == '__main__':
    solution = Solution()
    bin1 = '101' #0, carry 1, #0, carry 1, #0 carry 1, #1 5 + 3 = 8
    bin2 = '11'
    t = "1010"
    b = "1011"
    p = '1'

    print(solution.addBinary(t,b))
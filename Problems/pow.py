class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Taking a mathemtical approach, if n is odd, we can calculate x(base) times the base squared,
        to the power of ((n-1)/2). When n is even, we calculate the base squared to the power of (n/2).
        We repeat until 0.

        Credit to Issei_1, used for learning purposes.
        """
    def myPow(self, x: float, n: int) -> float:

        def function(base = x, exponent = abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        
        return float(f) if n >= 0 else 1/f
       
if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2.00000, -2))
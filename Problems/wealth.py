from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_max = 0
        for cust in accounts:
            wealth = 0
            for j in cust:
                wealth += j
            
            if wealth > wealth_max:
                wealth_max = wealth
                
        return wealth_max
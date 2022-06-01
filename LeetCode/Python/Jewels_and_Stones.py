class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_sum = 0 
        for i in jewels:
            jewel_sum = jewel_sum+ sum([1 for j in stones if i==j])      
        return jewel_sum
            

class Solution:
    def addDigits(self, num: int) -> int:
        sum_digits = num
        while(sum_digits>9):
            sum_digits = sum_to_str(sum_digits)
        return sum_digits
def sum_to_str(x):
    x =str(x)
    x = [int(i) for i in x]
    x = sum(x)
    return x
        

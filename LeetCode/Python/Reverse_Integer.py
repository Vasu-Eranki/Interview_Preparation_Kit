class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if(x<0):
            flag=1
        number = solution(abs(x),flag)
        number = power_shifter(number)
        return number
def power_shifter(number):
    greater = 2**31-1
    lower = -2**31
    if(number>greater) or (number<lower):
        number = 0
    return number

def solution(number,flag):
    result = 0
    while(number>0):
        remainder = number%10
        result = result*10+remainder
        number = number//10
    return result if flag==0 else -1*result

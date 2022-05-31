import math 
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend ==0):
            return 0
        elif(divisor ==1):
            return dividend
        else:  
            divid_log = math.log10(abs(dividend))
            divisor_log = math.log10(abs(divisor))
            if(divisor_log>divid_log):
                return 0
            orig_result = divid_log - divisor_log 
            result = math.floor(10**orig_result)
            if((math.ceil(10**orig_result)-(10**orig_result))<1e-5):
                print(math.ceil(10**orig_result),(10**orig_result))
                result = math.ceil(10**orig_result)
            if(divisor>0):
                if(dividend<0):
                    result = result*-1
            else:
                if(dividend>0):
                    result = result *-1
            return power_shifter(result)
def power_shifter(x):
    greater = 2**31-1
    lower = -2**31
    if(x>greater):
        x = greater
    elif(x<lower): 
        x= lower
    else:
        x = x
    return x

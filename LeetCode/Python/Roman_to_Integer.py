class Solution:
    def romanToInt(self, s: str) -> int:
        roman_sum = 0
        roman_dict ={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}
        roman_string = list(reversed(s))
        roman_sum += roman_dict[roman_string[0]]
        for i in range(1,len(roman_string)):
            number_1 = roman_dict[roman_string[i-1]]
            number_2 = roman_dict[roman_string[i]]
            if(number_1>number_2):
                roman_sum = roman_sum - number_2
            else:
                roman_sum = roman_sum + number_2
        return roman_sum
        

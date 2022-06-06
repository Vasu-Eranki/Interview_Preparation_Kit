class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {1000:'M',
                    900:'CM',
                    500:'D',
                    400:'CD',
                    100:'C',
                    90:'XC',
                    50:'L',
                    40:'XL',
                    10:'X',
                    9:'IX',
                    6:'VI',
                    5:'V',
                    4:'IV',
                    1:'I'}
        roman = to_roman(num,roman_dict)
        return roman

def to_roman(number,roman_dict):
    answer = ""
    for key in roman_dict.keys():
        quotient = number//key
        for i in range(quotient):
            answer+=roman_dict[key]
        number = number - quotient*key 
    return answer

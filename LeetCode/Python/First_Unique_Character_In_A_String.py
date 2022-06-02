class Solution:
    def firstUniqChar(self, s: str) -> int:
        string_dict=  {}
        flag = -1
        for i in range(0,len(s)):
            if(s[i] not in string_dict):
                string_dict[s[i]]=i
            else:
                string_dict[s[i]]= -1
        print(string_dict)
        for _,value in enumerate(string_dict):
            if(string_dict[value]!=-1):
                return string_dict[value]
        return -1
        

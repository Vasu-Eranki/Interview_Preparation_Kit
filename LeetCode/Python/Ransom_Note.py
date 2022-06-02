class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for i in magazine:
            if(i not in magazine_dict):
                magazine_dict[i] =1
            else:
                value = magazine_dict[i]
                magazine_dict[i] = value+1
        for i in ransomNote:
            if(i not in magazine_dict):
                return False
            else:
                value = magazine_dict[i]
                magazine_dict[i] = value -1 
        for key,value in enumerate(magazine_dict):
            if(magazine_dict[value]<0):
                return False
        return True

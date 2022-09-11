class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letters_dictionary = {}
        for i,j in zip(s,t):
            if(i not in letters_dictionary):
                letters_dictionary[i]=j
                if(check_for_duplicates(letters_dictionary)):
                    return False
            else:
                if(letters_dictionary[i]!=j):
                    return False
        return True
    
def check_for_duplicates(input_dict):
    keys = set(input_dict.keys())
    values = set(input_dict.values())
    return False if len(keys)==len(values) else True

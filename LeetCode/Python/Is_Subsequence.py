class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            index = find_first_index(i,t)
            if(index==-1):
                return False
            t = t[index:]
        return True
def find_first_index(a,b):
    for i in range(0,len(b)):
        if(b[i]==a):
            return i+1
    return -1

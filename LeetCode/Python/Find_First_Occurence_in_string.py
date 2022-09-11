class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start_pointer=0
        end_pointer = len(needle)
        while(start_pointer!=len(haystack)):
            if(haystack[start_pointer:start_pointer+end_pointer]==needle):
                return start_pointer
            else:
                start_pointer+=1;
        return -1

class Solution:
    def fib(self, n: int) -> int:
        result = fibonnacci_dynamic_programming(n)
        return result
    
def fibonnacci_dynamic_programming(n):
    if(n<2):
        return n
    else:
        answer = [0,1]
        for i in range(2,n+1):
            answer.append(answer[i-1]+answer[i-2])
        return answer[-1]

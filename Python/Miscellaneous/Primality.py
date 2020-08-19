def primechecker(n):
    if n==1:
        return "Not prime"
    elif n==2:
        return "Prime"
    else:
        if n%2==0:
            return "Not prime"
        else:
            flag = 0
            for i in range(3,round(n**0.5)+1,2):
                if n%i==0:
                    flag =1 
                    break
        return "Prime" if flag==0 else "Not prime"
number_of_cases = int(input())
for i in range(0,number_of_cases):
    x=int(input())
    answer = primechecker(x)
    print(answer)

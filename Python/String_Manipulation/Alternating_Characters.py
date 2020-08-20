#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    a=s.count('A')
    b=s.count('B')
    #print(a,b)
    if(a==0 or b==0):
        if(a!=0):
            return (a-1)
        else:
            return (b-1)
    else:
        count=1
        y=[1 if(s[i]==s[i+1]) else 0 for i in range(0,len(s)-1)]
        return sum(y)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()

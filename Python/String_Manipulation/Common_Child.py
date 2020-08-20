#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the commonChild function below.
def commonChild(s1, s2,x,y):
    L = [[None]*(y+1) for i in range(x+1)] 
    for i in range(x+1): 
        for j in range(y+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    return L[x][y] 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2,len(s1),len(s2))

    fptr.write(str(result) + '\n')

    fptr.close()

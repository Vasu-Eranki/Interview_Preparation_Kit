#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    total=0
    valley=0
    n_s=[1 if i=='U' else -1 for i in s]
    for i in n_s:
        total+=i
        if(i==1 and total==0):
            valley+=1
    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys
import collections 
from collections import deque
# Complete the rotLeft function below.
def rotLeft(a, d):
    a=deque(a)
    a.rotate(-d)
    return list(a)    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

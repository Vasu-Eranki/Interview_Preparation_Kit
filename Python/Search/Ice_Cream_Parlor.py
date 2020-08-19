#!/bin/python3

import math
import os
import random
import re
import sys


def whatFlavors(a, m):
    hs = { }
    for i in range(len(a)):
        if a[i] in hs:
            print(hs[a[i]], i + 1)
            break
        hs[m - a[i]] = i + 1
    
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)

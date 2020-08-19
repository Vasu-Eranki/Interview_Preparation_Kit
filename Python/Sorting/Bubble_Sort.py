#!/bin/python3
def bubblesort(a,n):
    swap = 0
    for i in range(0,n):
        for j in range(1,n):
            if(a[j-1]>a[j]):
                temp = a[j-1]
                temp1 = a[j]
                a[j-1]= temp1
                a[j]= temp
                swap+=1
    return swap,a[0],a[-1]            

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
(swaps,first,last) = bubblesort(a,n)
print("Array is sorted in",swaps,"swaps.")
print("First Element:",first)
print("Last Element:",last)

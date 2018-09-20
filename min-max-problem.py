#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum=0
    for n in arr:
        sum+=n
    minSum = sum-arr[0]
    maxSum = sum-arr[0]
    for n in arr[1:]:
        if sum-n<minSum:
            minSum=sum-n
        if sum-n>maxSum:
            maxSum=sum-n
    print(minSum,maxSum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

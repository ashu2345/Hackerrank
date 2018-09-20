#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    count=0
    maxN = 0
    for n in ar:
        if n > maxN:
            maxN = n
    while n in ar:
        ar.remove(n)
        count+=1
    return count

if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(result)

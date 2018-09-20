#!/bin/python3

import os
import sys

#
# Complete the xorMatrix function below.
#
def xorMatrix(m, first_row):
    matrix = []
    col = len(first_row)
    matrix.append(first_row)
    row = []
    for i in range(m-1):
        for j in range(col-1):
            row.append(first_row[j]^first_row[j+1])
        row.append(first_row[col-1]^first_row[0])
        first_row = row[:]
    return ' '.join(map(str,row))
    #
    # Write your code here.
    #
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    first_row = list(map(int, input().rstrip().split()))

    last_row = xorMatrix(m, first_row)

    print(last_row)

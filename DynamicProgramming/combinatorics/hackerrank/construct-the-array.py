#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
# https://www.youtube.com/watch?v=_nLeiMMSd4E

def countArray(n, k, x):
    if x != 1:
        endx = 0
        end = 1
    else:
        endx = 1
        end =0
    for i in range(2,n+1):
        endx, end = end, (end*(k-2) +endx*(k-1))%(1000000000+7)
    return endx % (10 ** 9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()

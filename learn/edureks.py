#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    countp=0
    countn=0
    countz=0
    for i in arr:
        if i < 0:
            countn+=1
        elif i > 0:
            countp+=1
        else:
            countz+=1
    x = (countp/n)
    y = (countn/n)
    z = (countz/n)
    print("{0:.6f}".format(x))
    print("{0:.6f}".format(y))
    print("{0:.6f}".format(z))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
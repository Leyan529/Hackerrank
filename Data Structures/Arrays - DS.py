'''
https://www.hackerrank.com/challenges/arrays-ds/problem

Sample Input
4
1 4 3 2

Output
2 3 4 1
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    b = []
    for idx in range(len(a)-1,-1,-1):
        b.append(a[idx])
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

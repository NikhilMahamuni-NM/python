c = [0, 0, 1, 0, 0, 1, 0]
jumps, i = 0, 0
while i < len(c)-1:
    # if 2 cloud jumps
    if i+2 < len(c) and c[i+2] != 1:
        i += 1
    jumps += 1
    i += 1
print(jumps)
'''
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    j=0
    i = 0
    while i < len(c)-1:
        if i+2 < len(c) and c[i+2] != 1:
            i += 1
        j += 1
        i += 1
    return j 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

'''

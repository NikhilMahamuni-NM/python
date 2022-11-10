
s = 'UDDDUDUU'

for step in s:
    inValley = False
    vallies = 0
    hgt = 0
    
    for step in s:
        if step == 'U':
            hgt += 1
        else:
            hgt -= 1            
        if not inValley:
            if hgt < 0:
                inValley = True
        elif hgt == 0:
            inValley = False
            vallies += 1
    
print(vallies)
'''
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = False
    no_val = 0
    height = 0
    
    for i in s:
        if i == 'U':
            height += 1
        else:
            height -= 1
        
        if not valley:
            if height < 0:
                valley = True
        elif height == 0:
            valley = False
            no_val +=1
    
    return no_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

'''

#Problem Statement:
#Given an array of integers, find the sum of its elements.


import math
import os
import random
import re
import sys

def simpleArraySum(ar):
    sum = 0

    for num in ar:
        sum += num

    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


    #Logic:
    #This code takes a list of numbers, starts with a total sum of 0, and then adds each number in the list to that sum. It returns the final sum, which is the sum of all the numbers in the list.
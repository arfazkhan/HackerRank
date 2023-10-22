#Problem Statement:
#In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    total_sum = 0

    for num in ar:
        total_sum += num

    return total_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#Logic:
#This code calculates the sum of all the numbers in a given list (ar). It initializes a variable total_sum to 0, then iterates through the list, adding each number to total_sum. Finally, it returns the total sum of all the numbers in the input list.
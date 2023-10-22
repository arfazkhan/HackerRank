#Problem Statement:
#https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true

def aVeryBigSum(ar):
    total_sum = 0

    for num in ar:
        total_sum += num

    return total_sum

#Logic:
#This code calculates the sum of all the numbers in a given list (ar). It initializes a variable total_sum to 0, then iterates through the list, adding each number to total_sum. Finally, it returns the total sum of all the numbers in the input list.
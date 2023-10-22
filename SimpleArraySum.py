#Problem Statement:
#https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true

def simpleArraySum(ar):
    sum = 0

    for num in ar:
        sum += num

    return sum

#Logic:
#, I'm given a list of numbers, and my task is to find their sum. To do this, I start with a sum of 0. Then, I loop through each number in the list and add it to the sum. Finally, I return the total sum. It's like adding up all the values in the list and giving back the result.
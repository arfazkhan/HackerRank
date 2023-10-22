#ProblemStatement:
#https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

def pickingNumbers(a):
    count_dict = {}
    max_length = 0

    for num in a:
        count_dict[num] = count_dict.get(num, 0) + 1

    for num in count_dict:
        max_length = max(max_length, count_dict[num] + count_dict.get(num + 1, 0))

    return max_length

#Logic:
#In this function, we're finding the longest subarray where the absolute difference between any two elements is at most 1. We create a dictionary to count the occurrences of each number in the array. Then, we iterate through the dictionary and check for the maximum length by considering the count of the current number and the count of the number one greater. This helps us find the maximum possible length of such a subarray
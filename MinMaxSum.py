#ProblemSatement:
# https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    
    print(min_sum, max_sum)


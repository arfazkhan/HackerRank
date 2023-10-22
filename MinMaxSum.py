#ProblemSatement:
#

def miniMaxSum(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    
    print(min_sum, max_sum)

#Logic:
#First, I sort the numbers in ascending order. Then, I find the sum of the smallest four numbers for the minimum sum and the sum of the largest four numbers for the maximum sum. Finally, I print these two sums.
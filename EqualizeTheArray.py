#ProblemStateent:
#https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true

def equalizeArray(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_count = max(count_dict.values())
    deletions = len(arr) - max_count
    return deletions


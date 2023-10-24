#https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true

def beautifulTriplets(d, arr):
    count = 0
    arr_set = set(arr)  
    for i in arr:
        if i + d in arr_set and i + 2 * d in arr_set:
            count += 1

    return count


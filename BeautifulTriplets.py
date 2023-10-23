#https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true

def beautifulTriplets(d, arr):
    count = 0
    arr_set = set(arr)  
    for i in arr:
        if i + d in arr_set and i + 2 * d in arr_set:
            count += 1

    return count

#Logic:
#I start by converting the array into a set for faster lookups. Then, I iterate over each element in the array. For each element, I check if the element incremented by 'd' and the element incremented by '2d' are both present in the set. If they are, it means I've found a beautiful triplet, so I increment my count. This approach allows me to find all beautiful triplets in the array with just a single pass, significantly improving the efficiency of the algorithm.
#https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true


def minimumDistances(a):
    min_distance = float('inf')  
    element_positions = {}  

    for i in range(len(a)):
        if a[i] in element_positions:
            distance = i - element_positions[a[i]]
            min_distance = min(min_distance, distance)
        element_positions[a[i]] = i

    if min_distance == float('inf'):
        return -1  
    else:
        return min_distance



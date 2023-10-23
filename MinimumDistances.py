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



#Logic:
#I start by initializing the minimum distance as infinity and creating an empty dictionary to store the last position of each element in the array. Then, I iterate over the array. For each element, I check if it’s already in the dictionary, which means I’ve seen it before. If it is, I calculate the distance between its current position and the last position where I saw it, and update the minimum distance if this new distance is smaller. Whether or not the element was in the dictionary, I update its last seen position in the dictionary to be its current position. After going through all elements, if the minimum distance is still infinity, it means I didn’t find any pair of identical elements, so I return -1. Otherwise, I return the minimum distance.

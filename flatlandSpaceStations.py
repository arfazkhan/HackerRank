#https://www.hackerrank.com/challenges/flatland-space-stations/problem

def flatlandSpaceStations(n, c):
    c.sort()
    max_distance = max(c[0], n - 1 - c[-1])
    
    for i in range(1, len(c)):
        max_distance = max(max_distance, (c[i] - c[i - 1]) // 2)
    
    return max_distance

#Logic:
#We begin by sorting the space station locations. We then calculate the maximum distance by considering the extreme cases - the distance from the first city to the first space station and from the last space station to the last city. These distances represent the initial maximums. Moving through the sorted space station locations, we calculate the maximum distance between adjacent stations and update our maximum if we find a longer distance. This method ensures an efficient exploration of the cityscape, identifying the farthest a city can be from the closest space station. The final value in the max_distance variable gives us this answer.
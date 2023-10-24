#https://www.hackerrank.com/challenges/flatland-space-stations/problem

def flatlandSpaceStations(n, c):
    c.sort()
    max_distance = max(c[0], n - 1 - c[-1])
    
    for i in range(1, len(c)):
        max_distance = max(max_distance, (c[i] - c[i - 1]) // 2)
    
    return max_distance

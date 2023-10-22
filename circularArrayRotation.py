#ProblemStatement:
#https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true

def circularArrayRotation(a, k, queries):
    n = len(a)
    effective_rotation = k % n
    rotated_positions = [(i - effective_rotation) % n for i in queries]
    result = [a[pos] for pos in rotated_positions]
    
    return result

#Logic:
#I'm simulating circular rotations in an array to answer specific queries. First, I calculate the effective rotation by finding the remainder of "k" divided by the array length. Then, for each query, I determine the final position after rotation by subtracting the effective rotation and taking the remainder with the array length. Then, I collect the values at these rotated positions and return them. It's like shifting the array in a circular manner and quickly responding to questions about its contents after rotation.
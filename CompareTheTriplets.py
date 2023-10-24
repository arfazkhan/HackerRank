#Problem Statement:
#https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0
    
    for i in range(3):
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
    
    return [alice_points, bob_points]


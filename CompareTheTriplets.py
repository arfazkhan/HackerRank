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

#Logic:
#I'm comparing two sets of scores of two players, Alice and Bob, and I'm keeping track of their points. I've got a loop that goes through three rounds, and in each round, I'm checking who scored higher. If Alice scores more than Bob in a round, I give a point to Alice. If Bob scores more, I give a point to Bob. So, I'm tallying up their scores round by round. In the end, I'm returning a list with two numbers. The first number is Alice's total points, and the second number is Bob's total points. 
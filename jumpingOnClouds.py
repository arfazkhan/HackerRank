#ProblemStatement:
#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true

def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100 
    current_cloud = 0

    while True:
        current_cloud = (current_cloud + k) % n
        energy -= 1

        if c[current_cloud] == 1:
            energy -= 2
        if current_cloud == 0:
            break  
    return energy

#Logic:
#In this code, we imagine simulating a game where I jump on clouds. I start with 100 units of energy. I iterate through clouds by jumping k steps at a time, looping back to the start if needed. For each jump, I decrease my energy by 1. If I land on a thundercloud (indicated by 1), I lose 2 energy. I repeat until I return to the initial cloud (cloud 0). The final energy level is my output, representing my energy after these jumps.

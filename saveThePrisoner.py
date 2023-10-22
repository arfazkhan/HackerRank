#ProblemStatement:
#https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true

def saveThePrisoner(n, m, s):
    remaining_sweets = m % n

    poisoned_prisoner = (s - 1 + remaining_sweets) % n
    if poisoned_prisoner == 0:
        poisoned_prisoner = n

    return poisoned_prisoner

#Logic:
#In this function, I'm determining which prisoner gets poisoned when distributing m sweets among n prisoners starting from prisoner s. First, I calculate the remaining sweets after distributing them equally among all prisoners using the modulo operation m mod n. Then, I find the position of the poisoned prisoner by adding the remaining sweets to the starting prisoner position (s−1) and taking the result n. If the calculated position is 0, indicating it exceeds the total number of prisoners, I set the poisoned prisoner to the last prisoner. This ensures a fair distribution of sweets among the prisoners and accurately identifies the prisoner who receives the poisoned sweet.
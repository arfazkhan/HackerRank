#ProblemStatement:
#
def saveThePrisoner(n, m, s):
    remaining_sweets = m % n

    poisoned_prisoner = (s - 1 + remaining_sweets) % n
    if poisoned_prisoner == 0:
        poisoned_prisoner = n

    return poisoned_prisoner

#Logic:

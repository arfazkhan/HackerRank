#ProblemStatement:
#https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    elif (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) >= 0:
        return "YES"
    else:
        return "NO"

#Logic:
#In this code, I'm helping two kangaroos, each starting at a different position and jumping with a specific distance. I want to know if they'll ever land on the same spot. First, I check if they have the same jumping distance; if they do, I check if they're already at the same position, and if they are, It will return "YES," indicating they'll meet. If their jumping distances are different, I calculate whether the relative distance between them and the relative speed allows them to meet at some point. If the claculations are correct, it will return "YES" otherwise "NO."
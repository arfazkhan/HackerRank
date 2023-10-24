#ProblemStatement:
# https://www.hackerrank.com/challenges/extra-long-factorials/submissions/code/352006714

def extraLongFactorials(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    print(a)


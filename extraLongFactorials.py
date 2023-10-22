#ProblemStatement:
# https://www.hackerrank.com/challenges/extra-long-factorials/submissions/code/352006714

def extraLongFactorials(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    print(a)

#Logic:
#I'm calculating and printing the factorial of a given number "n" I start with a value of 1 and then multiply it by each integer from 1 to "n" 

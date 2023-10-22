#roblemStatement:
#https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true

def staircase(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        hashes = "#" * i
        print(spaces + hashes)

#Logic:
#I'm creating a staircase pattern with n steps. To do this, I run a loop from 1 to n, and for each step, I calculate how many spaces and hashtags should be used. Then, I print the spaces and hashtags accordingly to form the staircase. 
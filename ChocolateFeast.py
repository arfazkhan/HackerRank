#https://www.hackerrank.com/challenges/chocolate-feast/problem?isFullScreen=true
def chocolateFeast(n, c, m):
    chocolates = wrappers = n // c

    while wrappers >= m:
        chocolates += wrappers // m
        wrappers = wrappers // m + wrappers % m

    return chocolates


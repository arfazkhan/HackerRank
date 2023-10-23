#https://www.hackerrank.com/challenges/chocolate-feast/problem?isFullScreen=true
def chocolateFeast(n, c, m):
    chocolates = wrappers = n // c

    while wrappers >= m:
        chocolates += wrappers // m
        wrappers = wrappers // m + wrappers % m

    return chocolates

#Logic:
# we start with the total number of chocolates being equal to the amount of money 'n' divided by the cost of a single chocolate 'c', and initially, the number of wrappers is the same. We continuously exchange wrappers for more chocolates while the number of wrappers is greater than or equal to 'm', where 'm' represents the number of wrappers required to get one more chocolate. With each exchange, we increment the chocolate count by the number of chocolates obtained by trading in wrappers (wrappers // m) and update the remaining wrappers by considering both those used in the trade (wrappers // m) and any leftover wrappers (wrappers % m). This process continues until there are no longer enough wrappers for another exchange. Finally, we return the total count of chocolates, considering both the initial purchase and all additional chocolates acquired through wrapper exchanges.
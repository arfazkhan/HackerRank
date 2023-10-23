#https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true
def howManyGames(p, d, m, s):
    count = 0
    current_price = p

    while s >= current_price:
        count += 1
        s -= current_price
        current_price = max(current_price - d, m)

    return count

#Logic:
#I start by setting the count of games I can buy to zero and the current price of the game to 'p'. Then, I enter a loop that continues as long as my remaining money 's' is greater than or equal to the current price. In each iteration of the loop, I increment my game count by one, subtract the current price from my money, and update the current price to be either its value minus 'd' or 'm', whichever is greater. This ensures that the price decreases by 'd' after each purchase until it reaches 'm'. The loop ends when I don't have enough money to buy a game at the current price. Finally, I return the count of games I can buy.
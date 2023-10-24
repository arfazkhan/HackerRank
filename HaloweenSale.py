def howManyGames(p, d, m, s):
    count = 0
    current_price = p

    while s >= current_price:
        count += 1
        s -= current_price
        current_price = max(current_price - d, m)

    return count


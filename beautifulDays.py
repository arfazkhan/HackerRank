def beautifulDays(i, j, k):
    beautiful_count = 0 
    for day in range(i, j + 1):

        reverse_day = int(str(day)[::-1])
        if abs(day - reverse_day) % k == 0:
            beautiful_count += 1
    
    return beautiful_count
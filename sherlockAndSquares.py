def squares(a, b):
    count = 0
    current = 1
    while True:
        square = current * current
        if square > b:
            break
        if square >= a and square <= b:
            count += 1
        current += 1
    return count
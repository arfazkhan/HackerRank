#ProblemStatement:
#https://www.hackerrank.com/challenges/sherlock-and-squares/submissions/code/352007292

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

#Logic:
# I'm counting the number of perfect squares that fall within a given range from a to b. I start with a count of 0 and increment a current number, checking its square in each iteration. If the square is within the range from a to b, I increment the count. When the square exceeds b, exit the loop. 
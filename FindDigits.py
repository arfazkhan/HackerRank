#ProblemStatement:
#https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true

def findDigits(n):
    count = 0  
    
    for digit in str(n):
        digit = int(digit)
        if digit != 0 and n % digit == 0:
            count += 1

    return count


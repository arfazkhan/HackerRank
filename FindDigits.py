#ProblemStatement:
#https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true

def findDigits(n):
    count = 0  
    
    for digit in str(n):
        digit = int(digit)
        if digit != 0 and n % digit == 0:
            count += 1

    return count

#Logic:
#In this function, I'm counting how many digits in a number evenly divide the number itself. I start with a count of zero and loop through each digit in the number. For each digit, I check if it's not zero and if dividing the number by the digit leaves no remainder. If both conditions are met, I increment the count. 
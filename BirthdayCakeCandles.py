#ProblemStatment:
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)    
    return count

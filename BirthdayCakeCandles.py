#ProblemStatment:
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)    
    return count

#Logic:
#I'm checking which candle is the tallest, and then I count how many candles have the same height as the tallest one.
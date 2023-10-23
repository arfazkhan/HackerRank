#https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true

def timeInWords(h, m):
    numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    if m == 0:
        return f"{numbers[h]} o' clock"
    
    if m == 15:
        return f"quarter past {numbers[h]}"
    
    if m == 30:
        return f"half past {numbers[h]}"
    
    if m == 45:
        return f"quarter to {numbers[h + 1]}"
    
    if m < 30:
        if m < 20:
            return f"{numbers[m]} {'minute' if m == 1 else 'minutes'} past {numbers[h]}"
        else:
            return f"twenty {numbers[m % 10]} {'minute' if m % 10 == 1 else 'minutes'} past {numbers[h]}"
    else:
        m = 60 - m
        if m < 20:
            return f"{numbers[m]} {'minute' if m == 1 else 'minutes'} to {numbers[h + 1]}"
        else:
            return f"twenty {numbers[m % 10]} {'minute' if m % 10 == 1 else 'minutes'} to {numbers[h + 1]}"

#Logic:
# I've created a list called numbers mapping integers to their word equivalents from "zero" to "nineteen" and special cases such as "quarter." The function takes two inputs, h for hours and m for minutes. The logic handles various cases: if m is 0, it returns the time in the format "{hour} o' clock." For other minutes, it checks if m corresponds to 15, 30, or 45 and outputs the time accordingly, like "quarter past," "half past," or "quarter to." For minutes less than 30, it converts the minutes to words, considering special cases and multiples of ten, and constructs the time with the words "past." For minutes greater than 30, it calculates the remaining minutes to the next hour, converts them to words, and constructs the time with the words "to." The function handles different minute scenarios and produces the time in words as per the given input hours and minutes.
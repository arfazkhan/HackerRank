#ProblemStatement:
#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true

def beautifulDays(i, j, k):
    beautiful_count = 0 
    for day in range(i, j + 1):

        reverse_day = int(str(day)[::-1])
        if abs(day - reverse_day) % k == 0:
            beautiful_count += 1
    
    return beautiful_count


#Logic:
#To count the number of "beautiful days" within a given range. First, we iterate through the range of days from "i" to "j." For each day, reverse its digits and check if the absolute difference between the day and its reverse is divisible by "k." If it is divisible, then it is a beautiful day and increment the count. At last, I return the count of beautiful days. It's all about identifying and counting those special days when the difference between a day and its reverse is a multiple of "k".

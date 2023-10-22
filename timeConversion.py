#ProblemStatement:
#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

def timeConversion(s):
    if s[-2:].lower() == 'pm':
        hours = (int(s[:2]) + 12) % 24
    else:
        hours = int(s[:2]) % 12

    return f"{hours:02d}{s[2:8]}"

#Logic:
#I'm converting time from 12-hour to 24-hour format. I quickly check if it's AM or PM by looking at the last two characters of the input string. If it's PM, I add 12 hours, if necessary and ensure the result stays within 24 hours. If it's AM, I convert the hours accordingly. Then, I format the output with leading zeros for a neat result. 
#ProblemStatement:
#https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true

def repeatedString(s, n):
    a_og = s.count('a')
    f_rep = n // len(s)
    r = n % len(s)
    a_par = s[:r].count('a')
    a_tot = (a_og * f_rep) + a_par

    return a_tot

#Logic:
# For calculating the number of occurrences of the letter 'a' in a repeated string. First, I count the occurrences of 'a' in the original string 's'. Then, I find how many times the string 's' repeats fully in the first 'n' characters and count the 'a's in these full repetitions. Next, I calculate the remaining characters after the full repetitions and count the additional 'a's in these. Finally, I sum up the 'a's from full repetitions and the remaining characters, giving the total count of 'a's in the repeated string of length 'n'. It's a systematic way to find the total occurrences of 'a' in the repeated string.

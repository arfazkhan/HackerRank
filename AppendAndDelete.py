#ProblemStatement:
#https://www.hackerrank.com/challenges/append-and-delete/submissions/code/352007089

def appendAndDelete(s, t, k):
    common_length = 0
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            break
        common_length += 1

    total_length = len(s) + len(t)
    delete = len(s) - common_length
    append = len(t) - common_length
    total = delete + append


    if k >= total and (k - total) % 2 == 0:
        return "Yes"
    elif k >= total_length:
        return "Yes"
    else:
        return "No"


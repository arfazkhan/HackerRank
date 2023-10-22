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

#Logic:
# For finding the common prefix length of two strings. First, I calculate total operations needed for deletion and appending. Then, to determine if it's possible within the given limit "k", I check if there are enough actions to cover the total changes. If the remaining actions after all changes are even, it returns "Yes." Additionally, if there are more actions available than the combined length of both strings, it also returns "Yes." Otherwise, it returns "No." It's all about ensuring I have the right moves to transform one string into another without interfering the prescribed limit.

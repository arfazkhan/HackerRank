#ProblemStatement:
#https://www.hackerrank.com/challenges/non-divisible-subset/problem 

def nonDivisibleSubset(k, s):
    remainder_count = [0] * k
    for num in s:
        remainder_count[num % k] += 1

    result = min(remainder_count[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            result += max(remainder_count[i], remainder_count[k - i])

    if k % 2 == 0:
        result += 1

    return result



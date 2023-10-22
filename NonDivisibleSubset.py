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


#logic:
# To dentify a non-divisible subset within a given list. We maintain an array to count the remainders of elements when divided by "k" Then, we calculate the result by considering the minimum of remainders that are evenly divisible by "k" and adding the maximum count for remainders that have complementary pairs. If "k" is even, add 1 to the result. This helps us find the largest non-divisible subset within the given list. It's about determining which elements can't be divided evenly by "k" and forming the largest possible subset from them.
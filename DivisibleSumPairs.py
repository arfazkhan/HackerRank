#ProblemStatement:
#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true
def divisibleSumPairs(n, k, ar):
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1

    return count

#Logic:
#In this code, I'm counting pairs of numbers in a list that are divisible by "k." I go through each possible pair, checking if their sum is evenly divisible by "k." If it is, then the count is incremented. So, The function efficiently finds these pairs, which helps me to count how many pairs satisfy this condition. It's like quickly searching for compatible pairs in the list.
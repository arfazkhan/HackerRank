#https://www.hackerrank.com/challenges/absolute-permutation/problem?isFullScreen=true
def absolutePermutation(n, k):
    if k == 0:
        return [i for i in range(1, n + 1)]
    if n % (2 * k) != 0:
        return [-1]

    ans = [-1] * n
    v = 1

    for i in range(0, n, 2 * k):
        for j in range(i + k, i + 2 * k):
            ans[j] = v
            v += 1
        for j in range(i, i + k):
            ans[j] = v
            v += 1

    return ans

#Logic:
# We're aiming to generate an absolute permutation, which is a rearrangement of the integers from 1 to n where each number is at a fixed distance k from its original position. First, we handle special cases: if k is zero, the permutation is simply the sequence from 1 to n. If n is not divisible by 2 * k, no absolute permutation is possible, so we return [-1].
# For valid cases, we create a list ans of size n to store our result. We iterate through the indices of this list. For each index i, we calculate the corresponding value for the absolute permutation. If the index allows, we place the value at the position i + k and fill the current position i with the value i + k + 1. By doing so, we ensure each number is at a distance k from its original position, creating a valid absolute permutation.
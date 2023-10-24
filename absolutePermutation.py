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
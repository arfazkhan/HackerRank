#ProblemStatement
#https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

s, t = (int(x) for x in input().strip().split())
a, b = (int(x) for x in input().strip().split())
m, n = (int(x) for x in input().strip().split())
apples = (int(x) for x in input().strip().split())
oranges = (int(x) for x in input().strip().split())

countA = sum(1 for d in apples if s <= a + d <= t)
countO = sum(1 for d in oranges if s <= b + d <= t)

print(countA)
print(countO)


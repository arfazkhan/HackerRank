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

#Logic
# In this code, First the values are read for the house and tree positions (s, t), the apple and orange tree positions (a, b), the number of apples and oranges (m, n), and the lists of apple and orange distances. Then, we count how many apples and oranges hit the house. If the distance from the tree (a or b) plus the fruit's distance (d) is within the range of the house (between s and t), we add 1 to the count. Finally, we get how many apples and oranges made it to the house

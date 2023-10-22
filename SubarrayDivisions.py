
#ProblemStatement:
#https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        segment = s[i:i+m]  # Get a contiguous segment of length m
        if sum(segment) == d:
            count += 1
    return count

#Logic:
# Initially, I take three inputs: a list s, which contains integers, and two integers d and m. The code initializes a count variable to 0 and uses a for loop to iterate through the list s, examining segments of length m. It ensures the loop stops before reaching the last m elements, ensuring there are enough elements to form a complete segment of length m. Inside the loop, the code extracts a contiguous segment of length m and calculates the sum of the elements within that segment using sum(segment). If the sum of the current segment equals the target value d, it increments the count by 1. Finally, the code returns the count, which represents the number of segments in the list s that have a sum equal to d and a length of m.
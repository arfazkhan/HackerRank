#ProblemStatement:
#https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    n = len(arr)  
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += arr[i][i]  
        secondary_diagonal_sum += arr[i][n - 1 - i]  

    result = abs(primary_diagonal_sum - secondary_diagonal_sum)

    return result

#Logic:
#I Imagined this code as a tool for a game board. In my approach, I look at each row and add the value from the main diagonal and its mirror position on the secondary diagonal. Then, I find the absolute difference between these sums. It's like comparing special moves in a game, helping me figure out which diagonal strategy is more powerful.
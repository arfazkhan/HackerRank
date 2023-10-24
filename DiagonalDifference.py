def diagonalDifference(arr):
    n = len(arr)  
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += arr[i][i]  
        secondary_diagonal_sum += arr[i][n - 1 - i]  

    result = abs(primary_diagonal_sum - secondary_diagonal_sum)

    return result


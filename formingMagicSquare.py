#ProblemStatement:
#https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true

def formingMagicSquare(s):
    magic_squares = [
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    ]

    min_cost = float('inf')

    for magic_square in magic_squares:
        cost = 0
        for i in range(3):
            for j in range(3):
                cost += abs(s[i][j] - magic_square[i][j])
        min_cost = min(min_cost, cost)

    return min_cost

#Logic:
#I have pre-defined magic squares and I compare the given square with each of them. For each comparison, I calculate the cost by finding the absolute differences between corresponding elements. The minimum cost among all magic squares is what I should be getting. It's like determining the most cost-effective way to convert the given square into a magic square
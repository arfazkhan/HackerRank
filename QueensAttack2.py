#ProblemStatement:
#https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true

def queensAttack(n, k, r_q, c_q, obstacles):
    attacked_squares = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    obstacle_set = {(obstacle[0], obstacle[1]) for obstacle in obstacles}
    for dx, dy in directions:
        x, y = r_q, c_q
        while True:
            x += dx
            y += dy
            if x > n or x < 1 or y > n or y < 1 or (x, y) in obstacle_set:
                break
            attacked_squares += 1
    return attacked_squares


#logic:
# For calculating the number of squares a queen can attack on an n×n chessboard. First define the possible directions a queen can move: horizontally, vertically, diagonally. Then,  use these directions to iterate through the board, considering obstacles. For each direction, move the queen until she encounters an obstacle, reaching the boundary, or completes the diagonal. Then count the squares she can attack in each direction and return the total. 
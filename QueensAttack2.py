
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
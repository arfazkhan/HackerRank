#https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true
def bomberMan(n, grid):
    new_grid = []
    for s in range(min(15,n+1)):
        for i in range(len(grid)):
            if s == 0: new_grid.append([])
            for j in range(len(grid[0])):
                if s == 0:
                    if grid[i][j] == ".":
                        new_grid[i].append(0)
                    else:
                        new_grid[i].append(1)
                elif s == 1:
                    if new_grid[i][j] > 0:
                        new_grid[i][j] += 1
                elif s > 1 and s % 2 == 0:
                    new_grid[i][j] += 1
                elif s > 2 and s % 2 == 1:
                    if new_grid[i][j] % 10 == 3:
                        new_grid[i][j] = 0
                        if i > 0: new_grid[i-1][j] = 0
                        if i+1 < len(grid): new_grid[i+1][j] += 10
                        if j > 0: new_grid[i][j-1] = 0
                        if j+1 < len(grid[0]): new_grid[i][j+1] += 10
                    elif new_grid[i][j] >= 10:
                        new_grid[i][j] = 0
                    else:
                        new_grid[i][j] += 1
        if s > 4:
            if s % 2 == 0 and n % 2 == 0:
                break
            if (s - 1) % 4 == 0 and (n - 1) % 4 == 0:
                break
            if (s - 3) % 4 == 0 and (n - 3) % 4 == 0:
                break

    result = []
    for i in range(len(new_grid)):
        result.append("")
        for j in range(len(new_grid[0])):
            result[i] += "." if new_grid[i][j] == 0 else "O"

    return result

#Logic:
# In this code, we're simulating a game where a character moves across a grid placing bombs. The grid initially contains either empty spaces represented by "." or bombs represented by "O." The character follows a specific pattern as they place bombs and wait for them to explode. We use the variable s to represent time steps, starting from 0.
# First, we initialize new_grid to keep track of the grid's state over time. Then, we go through each cell in the grid for each time step s.
# For s = 0, we initialize new_grid based on the current state of the grid. If a cell is empty, we set it to 0, and if it contains a bomb, we set it to 1.
# For s = 1, we increment the timer for cells that contain a bomb (value > 0).
# For s > 1, we handle the case when s is even and odd differently. For even s, we increment the timer for all cells. For odd s, we simulate bomb explosions by checking the timer values. If a cell's timer reaches 3, it explodes, affecting adjacent cells.
# The loop continues until s reaches the maximum of either 15 or n + 1. This ensures we capture the grid's state up to the given time n.
# At specific time steps (e.g., s > 4), we decide whether to break the loop based on conditions like the grid reaching a stable state or specific patterns.
# Finally, we create the result grid from new_grid, replacing timers with appropriate characters: 0 with ".", and any other value with "O."
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
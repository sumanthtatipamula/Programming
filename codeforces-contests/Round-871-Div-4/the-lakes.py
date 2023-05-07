def dfs(grid, i, j, r, c):
    if(i < 0 or j < 0 or i >= r or j >= c or grid[i][j] == 0 or grid[i][j] == -1):
        return 0
    depth = grid[i][j]
    grid[i][j] = -1
    for k, l in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        depth += dfs(grid, i + k, j + l, r, c)
    return depth


for _ in range(int(input())):
    r, c =  map(int, input().split())
    grid = [[0] * (c) for _ in range(r)]
    for i in range(r):
        grid[i] = [int(j) for j in input().strip().split(" ")]
    max_depth = 0
    for i in range(r):
        for j in range(c):
            if(grid[i][j] > 0):
                max_depth = max(max_depth, dfs(grid, i, j, r, c))
    print(max_depth)
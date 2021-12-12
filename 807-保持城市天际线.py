def maxIncreaseKeepingSkyline(grid):
    row = len(grid[0])
    col = len(grid)
    max_row = [max(grid[i]) for i in range(row)]
    max_col = [max([col_0[j] for col_0 in grid]) for j in range(col)]
    c = 0
    for i in range(col):
        for j in range(row):
            if min(max_row[i], max_col[j]) > grid[i][j]:
                c += min(max_row[i], max_col[j]) - grid[i][j]
    return c


print(maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7],[9, 2, 6, 3],[0, 3, 1, 0] ]))


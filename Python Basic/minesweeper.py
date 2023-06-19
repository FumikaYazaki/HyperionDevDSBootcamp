#Make a difinition
def minesweeper(grid):
    number = []
    #Iteration to check if each grid is adjacent to # 
    for row in range(len(grid)):
        number.append(grid[row][:])
        for col in range(len(grid[row])):
            #If the grid is #, do nothing
            if grid[row][col] == '#':
                continue
            #If the grid is not #, do following calculation 
            adjacent_grid = 0
            for i in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1),
                      (1, -1), (-1, 1)]:
                adjacent_row, adjacent_col = row + i[0], col + i[1]
                try:
                    if adjacent_row >= 0 and adjacent_col >= 0 and grid[adjacent_row][adjacent_col] == '#':
                        adjacent_grid += 1
                except IndexError:
                    pass
            number[row][col] = adjacent_grid
    return number

#Original grid
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
    ]

#Output
print(minesweeper(grid))
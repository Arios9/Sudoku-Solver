import numpy as np

grid = np.array([
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
])

def is_legal(i, j, num):
    for x in range(9):
        if grid[i][x] == num:
            return False
    for y in range(9):
        if grid[y][j] == num:
            return False
    sy = i//3*3
    sx = j//3*3
    for y in range(sy, sy+3):
        for x in range(sx, sx+3):
            if grid[y][x] == num:
                return False
    return True

solved = False

def solve():
    global solved                       
    if solved: return
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_legal(i, j, num):
                        grid[i][j] = num
                        solve()
                        grid[i][j] = 0
    if solved: return
    solved = True
    print(grid)

print("Problem")
print(grid)
print()
print("Solution")
solve()

import copy

f = open('day4/input.txt')
# f = open('day4/input_test.txt')


def count_adjecent(i, j, grid):
    c = 0
    for x in [i - 1, i, i + 1]:
        for y in [j - 1, j, j + 1]:
            if x < 0 or y < 0:
                continue
            if x >= len(grid) or y >= len(grid[0]):
                continue
            if x == i and y == j:
                continue
            if grid[x][y] == "@":
                c += 1
    return c


def process_grid(grid):
    grid2 = copy.deepcopy(grid)
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "@":
                continue
            c = count_adjecent(i, j, grid)
            if c < 4:
                total += 1
                grid2[i][j] = "x"
    if total == 0:
        return 0
    return total + process_grid(grid2)


grid = [list(line.strip()) for line in f.readlines()]
s = process_grid(grid)

print(s)

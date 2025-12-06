import math

f = open('input.txt')
# f = open('input_test.txt')


def process_grid(grid):
    n = len(grid[0])
    ops = grid[-1]
    numbers = grid[:-1]
    total = 0
    for i in range(n):
        if ops[i] == "+":
            total += sum(int(x[i]) for x in numbers)
        if ops[i] == "*":
            total += math.prod(int(x[i]) for x in numbers)

    return total


grid = [list(line.strip().split()) for line in f.readlines()]
s = process_grid(grid)

print(s)

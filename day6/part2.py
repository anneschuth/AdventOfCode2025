import math

f = open('input.txt')
# f = open('input_test.txt')


def process(op, nrs):
    if not op or not nrs:
        return 0
    transformed = []
    while any(nrs):
        nr = []
        for line in nrs:
            x = line.pop(0).strip()
            if x:
                nr.append(x)
        if nr:
            transformed.append(int(''.join(nr)))
    if op == "+":
        return sum(transformed)
    if op == "*":
        return math.prod(transformed)


lines = f.readlines()
nrlines = [list(line) for line in lines[:-1]]
print(nrlines)
operations = lines[-1]
print(operations)

op = None
n = len(lines) - 1
nrs = [[] for _ in range(n)]
total = 0
for c in operations:
    if c != " ":
        total += process(op, nrs)
        op = c
        nrs = [[] for _ in range(n)]

    for i, l in enumerate(nrlines):
        x = l.pop(0)
        nrs[i].append(x)

total += process(op, nrs)
print(total)

f = open('day3/input.txt')
# f = open('day3/input_test.txt')


def process_line(line):
    top = line[0:2]
    for x in line[2:]:
        if top[1] > top[0]:
            top.pop(0)
            top.append(x)
            continue
        if x > top[1]:
            top.pop(1)
            top.append(x)
            continue
    return int(''.join([str(x) for x in top]))

s = 0
for line in f:
    line = [int(x) for x in line.strip()]
    s += process_line(line)

print(s)

f = open('day3/input.txt')
# f = open('day3/input_test.txt')


def process_line(line):
    top = line[:12]
    for x in line[12:]:
        stop = False

        for y in range(1, len(top)):
            if top[y] > top[y - 1]:
                top[y - 1] = top[y]
                top.pop(y)
                top.append(x)
                stop = True
                break
        if stop:
            continue

        if x > top[-1]:
            top.pop(-1)
            top.append(x)
    return int(''.join([str(x) for x in top]))


s = 0
for line in f:
    line = [int(x) for x in line.strip()]
    s += process_line(line)

print(s)

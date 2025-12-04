f = open('day2/input.txt')
# f = open('day2/input_test.txt')


def is_invalid(pattern):
    n = len(pattern)
    for i in range(2, n+1):
        size, rest = divmod(n, i)
        if rest:
            continue
        part = pattern[:size]
        found = True
        for x in range(1, i):
            p = pattern[x * size:(x + 1) * size]
            if p != part:
                found = False
                break
        if found:
            return True
    return False


input = f.readline().split(",")
s = 0
for i in input:
    a, b = i.split("-", 1)
    invalids = []
    for x in range(int(a), int(b) + 1):
        if is_invalid(str(x)):
            s += int(x)
            invalids.append(x)

print(s)

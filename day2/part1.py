f = open('day2/input.txt')
# f = open('day2/input_test.txt')


def is_invalid(pattern):
    a, b = pattern[:len(pattern) // 2], pattern[len(pattern) // 2:]
    return a == b


input = f.readline().split(",")
s = 0
for i in input:
    a, b = i.split("-", 1)
    for x in range(int(a), int(b) + 1):
        if is_invalid(str(x)):
            s += int(x)
print(s)

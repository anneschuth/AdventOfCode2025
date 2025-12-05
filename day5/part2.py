f = open('day5/input.txt')
# f = open('day5/input_test.txt')

ranges = []
for line in f:
    line = line.strip()
    if "-" in line:
        a, b = line.split("-", 1)
        ranges.append((int(a), int(b)))
    else:
        break

ranges.sort()
prev_a, prev_b = ranges[0]
count = (prev_b - prev_a) + 1
for i, (a, b) in enumerate(ranges[1:]):
    if b <= prev_b:
        continue
    if a <= prev_b:
        a = prev_b + 1
    count += (b - a) + 1
    prev_a, prev_b = a, b

print(count)

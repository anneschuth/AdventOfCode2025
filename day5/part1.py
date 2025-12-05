f = open('day5/input.txt')
# f = open('day5/input_test.txt')

ranges = []
count = 0
for line in f:
    line = line.strip()
    if "-" in line:
        a, b = line.split("-", 1)
        ranges.append((int(a), int(b)))
    elif not line:
        continue
    else:
        x = int(line)
        for a, b in ranges:
            if a <= x <= b:
                count += 1
                break
print(count)

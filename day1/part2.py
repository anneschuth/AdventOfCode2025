f = open('day1/input.txt')
# f = open('day1/input_test.txt')

dial = 50
rotations = 0
for line in f:
    direction = line[0]
    ticks = int(line[1:])
    for t in range(ticks):
        if direction == "R":
            dial += 1
        elif direction == "L":
            dial -= 1
        dial %= 100
        if dial == 0:
            rotations += 1

print(rotations)

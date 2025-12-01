f = open('day1/input.txt')
# f = open('day1/input_test.txt')

dial = 50
rotations = 0
for line in f:
    direction = line[0]
    ticks = int(line[1:])
    if direction == "R":
        dial += ticks
    elif direction == "L":
        dial -= ticks
    dial %= 100
    if dial == 0:
        rotations += 1

    print(dial)

print(rotations)
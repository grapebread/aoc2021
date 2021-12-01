inp = open("../inp", 'r')

lines = [int(x) for x in inp.readlines()]
prev = sum(lines[:3])
count = 0

for i in range(len(lines) - 2):
    n = sum(lines[i:i+3])
    if (n > prev):
        count += 1
    prev = n

print(count)
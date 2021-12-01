inp = open("../inp", 'r')

prev = int(inp.readline())
count = 0

for line in inp:
    if (int(line) > prev):
        count += 1
    prev = int(line)

print(count)
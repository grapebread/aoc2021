inp = open("../inp", "r")
lines = [x.strip() for x in inp.readlines()]


gamma, epsilon = "", ""
size = len(lines[0])

for i in range(size):
    arr = [line[i] for line in lines]

    n = arr.count('1') > arr.count('0')
    gamma += '1' if n else '0'
    epsilon += '0' if n else '1'

print(int(gamma, 2) * int(epsilon, 2))
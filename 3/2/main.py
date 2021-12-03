from copy import deepcopy

inp = open("../inp", "r")

co2 = [line.strip() for line in inp.readlines()]
oxy = deepcopy(co2)

size = len(oxy[0])

for i in range(size):
    oxy_arr = [line[i] for line in oxy]
    oxy_n2 = 0
    oxy_n1 = [oxy_arr.count('1'), oxy_arr.count('0')]
    if oxy_n1[0] == oxy_n1[1]:
        oxy_n2 = 1
    else:
        if oxy_n1[0] > oxy_n1[1]:
            oxy_n2 = 1
        else:
            oxy_n2 = 0

    if len(oxy) == 1:
        break
    else:
        oxy = [line for line in oxy if int(line[i]) == oxy_n2]

for i in range(size):
    co2_arr = [line[i] for line in co2]
    co2_n2 = 0
    co2_n1 = [co2_arr.count('1'), co2_arr.count('0')]

    if co2_n1[0] == co2_n1[1]:
        co2_n2 = 0
    else:
        if co2_n1[0] > co2_n1[1]:
            co2_n2 = 0
        else:
            co2_n2 = 1

    if len(co2) == 1:
        break
    else:
        co2 = [line for line in co2 if int(line[i]) == co2_n2]

print(int(oxy[0], 2) * int(co2[0], 2))
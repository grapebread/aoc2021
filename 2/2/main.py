inp = open("../inp", 'r')
lines = [(x.split(" ")[0], int(x.split(" ")[1])) for x in inp.readlines()]

aim = 0
hori = 0
vert = 0

for action in lines:
    if action[0] == "forward":
        hori += action[1]
        vert += (aim * action[1])
    elif action[0] == "up":
        aim -= action[1]
    else:
        aim += action[1]

print(hori * vert)
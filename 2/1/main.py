inp = open("../inp", 'r')
lines = [(x.split(" ")[0], int(x.split(" ")[1])) for x in inp.readlines()]

hori = 0
vert = 0

for action in lines:
    if action[0] == "forward":
        hori += action[1]
    elif action[0] == "up":
        vert -= action[1]
    else:
        vert += action[1]

print(hori * vert)

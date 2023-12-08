import math

f = open("08.txt","r").read().split("\n")
ins = f[0]
m = {i[0:3] : [i[7:10], i[12:15]] for i in f[2:]}

starts = [i for i in m.keys() if i[2] == "A"]
steps = []

for curr in starts:
    r = 0
    while True:
        curr = m[curr][ins[r % len(ins)] == "R"]
        r += 1
        if curr[2] == "Z":
            break
    steps.append(r)

print(math.lcm(*steps))
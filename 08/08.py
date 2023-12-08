f = open("08.txt","r").read().split("\n")
ins = f[0]
m = {i[0:3] : [i[7:10], i[12:15]] for i in f[2:]}

curr = "AAA"
r = 0
while True:
    curr = m[curr][ins[r % len(ins)] == "R"]
    r += 1
    if curr == "ZZZ":
        break

print(r)
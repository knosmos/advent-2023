def hash(i):
    k = 0
    for c in i:
        k += ord(c)
        k = (k * 17) % 256
    return k

curr = [[] for _ in range(256)]
for i in open("15.txt", "r").read().split(","):
    if "-" in i:
        i = i[:-1]
        box = hash(i)
        for k, it in enumerate(curr[box]):
            if it[0] == i:
                curr[box].pop(k)
                break
    else:
        i, lens = i.split("=")
        box = hash(i)
        for k, it in enumerate(curr[box]):
            if it[0] == i:
                curr[box][k][1] = int(lens)
                break
        else:
            curr[box].append([i, int(lens)])

r = 0
for i, box in enumerate(curr):
    for j, lens in enumerate(box):
        r += (i + 1) * (j + 1) * lens[1]
print(r)
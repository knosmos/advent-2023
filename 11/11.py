f = open("11.txt","r").read().split("\n")

u_r = [0] * len(f) # unvisited
u_c = [0] * len(f[0])
for r, row in enumerate(f):
    for c, char in enumerate(row):
        if char == "#":
            u_r[r] = 1
            u_c[c] = 1
off_r = 0 # offset counter for row
g = []
for r, row in enumerate(f):
    off_c = 0 # offset counter for column
    for c, char in enumerate(row):
        if char == "#":
            g.append((r + off_r, c + off_c)) # actual position of galaxy
        if u_c[c] == 0:
            off_c += 1
    if u_r[r] == 0:
        off_r += 1

def dist(a, b): # manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

r = 0
for i in g:
    r += sum([dist(i, j) for j in g])
print(r // 2)
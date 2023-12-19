x = 0
y = 0
perim = 0
pts = [(0, 0)]
for i in open("18.txt").read().split("\n"):
    k = i.split()[2][2:]
    n = int(k[:5], 16)
    d = k[5]
    if d == "0": x += n
    if d == "2": x -= n
    if d == "3": y -= n
    if d == "1": y += n
    pts.append((x, y))
    perim += n

# shoelace formula
a = 0
for i in range(len(pts)):
    a += pts[i][0] * pts[(i+1)%len(pts)][1]
    a -= pts[i][1] * pts[(i+1)%len(pts)][0]
a = abs(a) // 2

# black magic pick's theorem
print(a + perim // 2 + 1)
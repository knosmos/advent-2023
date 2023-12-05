from collections import deque

f = open("05.txt", "r").read()
#f = open("05.txt", "r").read().split("\n")

maps = f.split("\n\n")

q = deque([1, int(i)] for i in maps[0].split(": ")[1].split())

def conv(o, m):
    for i in m.split("\n")[1:]:
        a, b, c = map(int, i.split())
        if o >= b and o < b + c:
            return a + (o - b)
    return o

res = []
while q:
    l, o = q.popleft()
    if l == 8:
        res.append(o)
        continue
    else:
        q.append([l+1, conv(o, maps[l])])

print(min(res))
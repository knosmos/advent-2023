from heapq import *
g = [list(map(int, list(i))) for i in open("17.txt", "r").read().split("\n")]
mem = {(0, 0, 0, 0, 0): 0}
q = [(0, 0, 0, 0, 0, 0)]
while q:
    prev, x, y, cx, cy, p = heappop(q)
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        if dx == -cx and dy == -cy:
            continue
        if dx == cx and dy == cy:
            pos = [x+dx, y+dy]
            if pos[0] >= len(g[0]) or pos[1] >= len(g) or pos[0] < 0 or pos[1] < 0:
                continue
            nxt = [prev + g[y+dy][x+dx], x+dx, y+dy, dx, dy, p+1]
        else:
            pos = [x+dx*4, y+dy*4]
            if pos[0] >= len(g[0]) or pos[1] >= len(g) or pos[0] < 0 or pos[1] < 0:
                continue
            nxt = [prev + sum([g[y+dy*i][x+dx*i] for i in range(1, 5)]), x+dx*4, y+dy*4, dx, dy, 4]
        if nxt[5] > 10:
            continue
        f = False
        for i in range(4, nxt[5]+1):
            if (nxt[1], nxt[2], nxt[3], nxt[4], i) in mem and mem[(nxt[1], nxt[2], nxt[3], nxt[4], i)] <= nxt[0]:
                f = True
                break
        if f:
            continue
        #print(nxt)
        #print(mem)
        mem[tuple(nxt[1:])] = nxt[0]
        heappush(q, nxt)
r = float("inf")
for k, v in mem.items():
    if k[0] == len(g[0])-1 and k[1] == len(g)-1:
        r = min(r, v)
print(r)
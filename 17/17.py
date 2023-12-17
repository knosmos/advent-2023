from heapq import heappush, heappop
g = [list(map(int, list(i))) for i in open("17.txt", "r").read().split("\n")]
mem = {(0, 0, 0, 0, 0): 0}
q = [(0, 0, 0, 0, 0, 0)]
while q:
    prev, x, y, cx, cy, p = heappop(q)
    for nxt in [[x+1, y, 1, 0], [x, y+1, 0, 1], [x-1, y, -1, 0], [x, y-1, 0, -1]]:
        if nxt[0] >= len(g[0]) or nxt[1] >= len(g) or nxt[0] < 0 or nxt[1] < 0:
            continue
        if nxt[2] == -cx and nxt[3] == -cy:
            continue
        if nxt[2] == cx and nxt[3] == cy:
            nxt.append(p+1)
        else:
            nxt.append(0)
        if nxt[4] > 2:
            continue
        cst = prev + g[nxt[1]][nxt[0]]
        f = False
        for i in range(nxt[4]+1):
            if (nxt[0], nxt[1], nxt[2], nxt[3], i) in mem and mem[(nxt[0], nxt[1], nxt[2], nxt[3], i)] <= cst:
                f = True
                break
        if f: continue
        mem[tuple(nxt)] = cst
        heappush(q, tuple([cst] + nxt))
r = float("inf")
for k, v in mem.items():
    if k[0] == len(g[0])-1 and k[1] == len(g)-1:
        r = min(r, v)
print(r)
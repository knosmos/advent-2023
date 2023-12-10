from collections import deque
m = open("10.txt", "r").read().split("\n")

# find S
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == "S":
            S = (i, j)
dist = [[0 for i in range(len(m[0]))] for j in range(len(m))]
dist[S[0]][S[1]] = 0

# bfs
q = [S]
vis = [[False for i in range(len(m[0]))] for j in range(len(m))]
vis[S[0]][S[1]] = True
while q:
    r, c = q.pop(0)
    nxt = []
    if m[r][c] == "S":
        if m[r+1][c] in "JL|":
            nxt.append((r+1, c))
        if m[r][c-1] in "FL-":
            nxt.append((r, c-1))
        if m[r][c+1] in "J7-":
            nxt.append((r, c+1))
        if m[r-1][c] in "F7|":
            nxt.append((r-1, c))
    if m[r][c] == "J":
        nxt = [(r-1, c), (r, c-1)]
    if m[r][c] == "L":
        nxt = [(r, c+1), (r-1, c)]
    if m[r][c] == "F":
        nxt = [(r+1, c), (r, c+1)]
    if m[r][c] == "7":
        nxt = [(r+1, c), (r, c-1)]
    if m[r][c] == "|":
        nxt = [(r+1, c), (r-1, c)]
    if m[r][c] == "-":
        nxt = [(r, c+1), (r, c-1)]
    for i in nxt:
        if i[0] < 0 or i[1] < 0 or i[0] >= len(m) or i[1] >= len(m[0]):
            continue
        if vis[i[0]][i[1]] == False:
            vis[i[0]][i[1]] = True
            dist[i[0]][i[1]] = dist[r][c] + 1
            q.append(i)
# ray throwing
ret = 0
k = [["." for i in range(len(m[0]))] for j in range(len(m))]
for r in range(len(m)):
    for c in range(len(m[0])):
        if vis[r][c]:
            continue
        cnt = 0
        i = r
        while i < len(m):
            if vis[i][c]:
                if m[i][c] != "|":
                    cnt += 1
                if m[i][c] == "F":
                    while i < len(m):
                        if vis[i][c]:
                            if m[i][c] == "J":
                                break
                            if m[i][c] == "L":
                                cnt -= 1
                                break
                        i += 1
                if m[i][c] == "7":
                    while i < len(m):
                        if vis[i][c]:
                            if m[i][c] == "L":
                                break
                            if m[i][c] == "J":
                                cnt -= 1
                                break
                        i += 1
            i += 1
        k[r][c] = cnt
        if cnt % 2 == 1:
            ret += 1
print("\n".join(["".join(["#" if i else "." for i in j]) for j in vis]))
print("\n".join([" ".join([str(i) for i in j]) for j in k]))
print(ret)
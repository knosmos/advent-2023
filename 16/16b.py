g = open("15.txt", "r").read().split("\n")

def solve(initial):
    vis = [[False for _ in range(len(g[0]))] for _ in range(len(g))]
    seen = set()
    s = [initial] # (x, y, dx, dy)
    while s:
        x, y, dx, dy = s.pop()
        # test validity
        if x < 0 or y < 0 or x >= len(g[0]) or y >= len(g):
            continue
        if (x, y, dx, dy) in seen:
            continue
        seen.add((x, y, dx, dy))
        vis[y][x] = True
        if g[y][x] == ".":
            s.append((x+dx, y+dy, dx, dy))
        elif g[y][x] == "|":
            if dx == 1 or dx == -1:
                s.append((x, y+1, 0, 1))
                s.append((x, y-1, 0, -1))
            else:
                s.append((x+dx, y+dy, dx, dy))
        elif g[y][x] == "-":
            if dy == 1 or dy == -1:
                s.append((x+1, y, 1, 0))
                s.append((x-1, y, -1, 0))
            else:
                s.append((x+dx, y+dy, dx, dy))
        elif g[y][x] == "\\":
            if dx == 1: # right
                s.append((x, y+1, 0, 1))
            elif dx == -1: # left
                s.append((x, y-1, 0, -1))
            elif dy == 1: # down
                s.append((x+1, y, 1, 0))
            elif dy == -1: # up
                s.append((x-1, y, -1, 0))
        elif g[y][x] == "/":
            if dx == 1:
                s.append((x, y-1, 0, -1))
            elif dx == -1:
                s.append((x, y+1, 0, 1))
            elif dy == 1:
                s.append((x-1, y, -1, 0))
            elif dy == -1:
                s.append((x+1, y, 1, 0))
    return sum(sum(row) for row in vis)

r = 0
# horiz edges
for i in range(len(g[0])):
    r = max(r, solve((i, 0, 0, 1)))
    r = max(r, solve((i, len(g)-1, 0, -1)))

# vert edges
for i in range(len(g)):
    r = max(r, solve((0, i, 1, 0)))
    r = max(r, solve((len(g[0])-1, i, -1, 0)))

print(r)
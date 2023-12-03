g = open("03.txt","r").read().split("\n")
s = set()
ge = {}
r = 0
for i, line in enumerate(g):
    for j, char in enumerate(line):
        if char == "*":
            s.add((i,j))
            ge[(i,j)] = set()
def adj(x, y, s):
    return {(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x-1,y-1),(x+1,y-1),(x-1,y+1)} & s
for i, line in enumerate(g):
    curr_num = None
    l = 0
    for j, char in enumerate(line):
        if char.isnumeric():
            curr_num = curr_num*10 + int(char) if curr_num != None else int(char)
            l += 1
        else:
            for k in range(j-l, j):
                for f in adj(i, k, s):
                    ge[f].add(curr_num)
            curr_num = None
            l = 0
    if curr_num != None:
        for k in range(j-l, j):
            for f in adj(i, k, s):
                ge[f].add(curr_num)
for i in ge:
    if len(ge[i]) == 2:
        r += list(ge[i])[0] * list(ge[i])[1]
print(ge)
print(r)
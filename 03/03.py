g = open("03.txt","r").read().split("\n")
s = set()
r = 0
for i, line in enumerate(g):
    for j, char in enumerate(line):
        if char != "." and not char.isnumeric():
            s.add((i,j))
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
                print(i, k, adj(i, k, s))
                if adj(i, k, s):
                    r += curr_num
                    break
            print(curr_num)
            curr_num = None
            l = 0
    if curr_num != None:
        for k in range(j-l, j):
            if adj(i, k, s):
                r += curr_num
                break
print(s)
print(r)
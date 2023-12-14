def solve(row):
    curr_offset = 0
    r = 0
    x = ""
    for i in range(len(row)):
        if row[i] == "#":
            x += "." * (i - curr_offset)
            curr_offset = i + 1
            x += "#"
        elif row[i] == "O":
            r += len(row) - curr_offset
            curr_offset += 1
            x += "O"
    # pad
    x += "." * (len(row) - curr_offset)
    return r, x

def render(p, r):
    k = list(zip(*p[::-1]))
    for i in range(4 - r % 4 + 2):
        k = list(map(list, zip(*k[::-1])))
    k = list(map(list, zip(*k)))
    print("\n".join("".join(row) for row in k))
    print()

p = open("14.txt","r").read().split("\n")

# transpose
p = list(map(list, zip(*p)))

# simulate
for i in range(4*1000):
    np = []
    for row in p:
        r, x = solve(row)
        np.append(x)
    p = np
    p = list(zip(*p))[::-1]
    #render(p, i)

r = 0
for row in p:
    for i, c in enumerate(row):
        if c == "O":
            r += len(row) - i
print(r)
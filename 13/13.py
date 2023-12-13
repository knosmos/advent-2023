def process(p):
    # horizontal
    for y in range(1, len(p)):
        s = max(0, y - (len(p) - y))
        for x in range(s, y + 1):
            # match
            if p[x] != p[y + (y-x) - 1]:
                break
        else:
            return y * 100

    # vertical
    p = list(map(list, zip(*p)))    # transpose p
    for y in range(1, len(p)):
        s = max(0, y - (len(p) - y))
        for x in range(s, y + 1):
            # match
            if p[x] != p[y + (y-x) - 1]:
                break
        else:
            return y

    return "something is seriously wrong"

# main
r = 0
for p in open("13.txt", "r").read().split("\n\n"):
    p = p.split("\n")
    r += process(p)
print(r)
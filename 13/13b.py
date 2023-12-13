def match(p):
    # find lines of reflection
    k = []
    for y in range(1, len(p)):
        s = max(0, y - (len(p) - y))
        for x in range(s, y + 1):
            # match
            if p[x] != p[y + (y-x) - 1]:
                break
        else:
            k.append(y)
    return k

def process(p):
    # find original line of reflection
    # horizontal
    a = match(p)
    if a:
        original = ["h", a[0]]
    else:
        # vertical
        p2 = list(map(list, zip(*p))) # transpose p
        b = match(p2)[0]
        original = ["v", b]

    for i in range(len(p)):
        for j in range(len(p[i])):
            # flip one squre
            p[i][j] = 1 - p[i][j]

            # test for lines of reflection
            # horizontal
            a2 = match(p)
            oth = set(a2) - {original[1]}
            if a2:
                if original[0] != "h":
                    return a2[0] * 100
                elif len(oth) >= 1:
                    return list(oth)[0] * 100
            # vertical
            b2 = match(list(map(list, zip(*p))))
            oth = set(b2) - {original[1]}
            if b2:
                if original[0] != "v":
                    return b2[0]
                elif len(oth) >= 1:
                    return list(oth)[0]

            # put that thing back where it came from or so help me
            p[i][j] = 1 - p[i][j]

# main
r = 0
for p in open("13.txt", "r").read().split("\n\n"):
    p = list(map(lambda k:[int(i == "#") for i in k], p.split("\n")))
    r += process(p)
print(r)
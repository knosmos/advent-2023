def extra(seq):
    diffs = []
    d = seq
    while any(d):
        diffs.append(d)
        d = [d[i] - d[i-1] for i in range(1, len(d))]
    print(diffs)
    return sum([i[-1] for i in diffs])

r = 0
for i in open("09.txt", "r").read().split("\n"):
    seq = list(map(int, i.split()))
    r += extra(seq)

print(r)
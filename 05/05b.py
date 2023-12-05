f = open("05.txt").read().split("\n\n")
seeds = list(map(int, f[0].split(": ")[1].split()))
rs = [[seeds[i], seeds[i] + seeds[i+1] - 1] for i in range(0, len(seeds), 2)]
#print(rs)
for lvl in range(7):
    nrs = []
    m = [list(map(int, i.split())) for i in f[lvl+1].split("\n")[1:]]
    for a in rs:
        for ma in m:
            # get part of range a that overlaps with map ma
            dest, sta, cnt = ma
            b = [sta, sta + cnt - 1]
            if b[0] > a[1] or a[0] > b[1]:
                continue
            # calculate intersection
            nrs.append([
                max(a[0], b[0]) + (dest - sta),
                min(a[1], b[1]) + (dest - sta)
            ])
            # calculate anti intersection
            l = [a[0], max(a[0], b[0])-1]
            r = [min(a[1], b[1])+1, a[1]]
            if l[0] <= l[1]:
                rs.append(l)
            if r[0] <= r[1]:
                rs.append(r)
            break
        else:
            nrs.append(a)
    #print(nrs)
    rs = nrs
print(min(rs, key=lambda i:i[0])[0])
l = open("04.txt","r").read().split("\n")
r = 0
for line in l:
    a,b = line.split(": ")[1].split("|")
    a = list(map(int,a.split()))
    b = list(map(int,b.split()))
    k = len(set(a) & set(b))
    r += 2 ** (k-1) if k > 0 else 0
print(r)
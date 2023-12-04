l = open("04.txt","r").read().split("\n")
v = []
for i, line in enumerate(l):
    a,b = line.split(": ")[1].split("|")
    a = list(map(int,a.split()))
    b = list(map(int,b.split()))
    k = len(set(a) & set(b))
    v.append([i, k])
from collections import deque
q = deque(v)
r = 0
while q:
    i, k = q.popleft()
    r += 1
    for j in range(i+1, i+k+1):
        q.append([j, v[j][1]])
print(r)
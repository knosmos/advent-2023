r = 0
for i in open("15.txt", "r").read().split(","):
    k = 0
    for c in i:
        k += ord(c)
        k = (k * 17) % 256
    r += k
print(r)
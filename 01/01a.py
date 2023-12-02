a = 0
k = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i in open("01.txt","r").read().split("\n"):
    r = []
    for j, char in enumerate(i):
        if char.isnumeric():
            r.append(int(char))
        for c in k:
            if i[j:].startswith(c):
                r.append(k.index(c)+1)
    a += r[0]*10 + r[-1]
print(a)
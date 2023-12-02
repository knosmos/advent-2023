a = 0
k = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i in open("01.txt","r").read().split("\n"):
    last = ""
    x = []
    for j, char in enumerate(i):
        w = True
        while w:
            for l in k:
                if l.startswith(last):
                    w = False
                    break
            else:
                last = last[1:]
        last += char
        if last in k:
            x.append(k.index(last)+1)
        elif char.isnumeric():
            x.append(char)
            last = ""
    print(x)
    a += int(x[0])*10 + int(x[-1])
print(a)